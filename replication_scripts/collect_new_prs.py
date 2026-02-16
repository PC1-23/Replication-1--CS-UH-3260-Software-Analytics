import requests
import csv
import time
import os
from config import GITHUB_TOKEN


TOKEN = GITHUB_TOKEN  

REPOS = [
    'grpc/grpc-java',
    'JabRef/jabref', 
    'apache/accumulo',
    'gradle/gradle',
    'netty/netty'
]

KEYWORDS = [
    'readability', 'readable', 
    'understandability', 'understandable',
    'clarity', 'legibility',
    'easier to read', 'comprehensible'
]

def query_github(search_term):
    headers = {'Authorization': f'Bearer {TOKEN}'}
    
    query = """
    query {
        search(query: "%s", type: ISSUE, first: 100) {
            issueCount
            edges {
                node {
                    ... on PullRequest {
                        number
                        url
                        title
                        body
                        mergedAt
                        mergedBy { login }
                        author { login }
                        comments(last: 100) {
                            edges {
                                node {
                                    bodyText
                                }
                            }
                        }
                        commits(last: 100) {
                            edges {
                                node {
                                    commit {
                                        message
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    """ % search_term
    
    response = requests.post(
        'https://api.github.com/graphql',
        json={'query': query},
        headers=headers
    )
    return response.json()


def get_prs(repo):
    """Get all PRs for a repo"""
    print(f"\nProcessing {repo}...")
    results = []
    
    for kw in KEYWORDS:
        search = f'{kw} repo:{repo} is:pr is:merged review:approved merged:2021-01-01..2026-02-15'        
        try:
            data = query_github(search)
            count = data['data']['search']['issueCount']
            print(f"  {kw}: {count} PRs")
            
            for edge in data['data']['search']['edges']:
                pr = edge['node']
                
                comments = [c['node']['bodyText'] for c in pr['comments']['edges'] if c['node']['bodyText']]
                
                commits = [c['node']['commit']['message'] for c in pr['commits']['edges']]
                
                pr_data = {
                    'repo': repo,
                    'number': pr['number'],
                    'url': pr['url'],
                    'title': pr['title'],
                    'body': pr['body'] or '',
                    'merged': pr['mergedAt'],
                    'merged_by': pr['mergedBy']['login'] if pr['mergedBy'] else '',
                    'author': pr['author']['login'] if pr['author'] else '',
                    'keywords': kw,
                    'comments': ' | '.join(comments),
                    'commits': ' | '.join(commits)
                }
                
                results.append(pr_data)
            
            time.sleep(1)  
            
        except Exception as e:
            print(f"  ERROR: {e}")
    
    return results


print("Starting collection...")
all_prs = []

for repo in REPOS:
    prs = get_prs(repo)
    all_prs.extend(prs)
    print(f"Got {len(prs)} PRs from {repo}")

print(f"\nTotal: {len(all_prs)} PRs")

unique = {}
for pr in all_prs:
    url = pr['url']
    if url not in unique:
        unique[url] = pr
    else:
        if pr['keywords'] not in unique[url]['keywords']:
            unique[url]['keywords'] += ', ' + pr['keywords']

final = list(unique.values())
print(f"After dedup: {len(final)} unique PRs")

with open('new_prs_2021_2026.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=final[0].keys())
    writer.writeheader()
    writer.writerows(final)

print("Saved to new_prs_2021_2026.csv")
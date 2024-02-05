import pandas as pd
from TiktokApi import TiktokApi

# For example (taylorswift): MS4wLjABAAAAqB08cUbXaDWqbD6MCga2RbGTuhfO2EsHayBYx08NDrN7IE3jQuRDNNN6YwyfH6_6
USER_SEC_UID = 'YOUR_USER_SEC_UID'
COUNT = 5000

if __name__ == '__main__':
  results = []
  
  tiktok = TiktokApi()
  minCursor = 0
  maxCursor = 0
  
  while (minCursor != -1 and maxCursor != -1) and len(results) < COUNT:
    response = tiktok.get_user_followers(
      USER_SEC_UID,
      minCursor,
      maxCursor
    )

    if not response:
      minCursor = -1
      maxCursor = -1
      break
    
    results.extend(response.get('followers'))
    minCursor = response.get('minCursor')
    maxCursor = response.get('maxCursor')

  if len(results) > 0:
    df = pd.DataFrame(results)
    df.to_excel(f'{USER_SEC_UID}.xlsx', index=False)

  print('Done')

import requests

class TiktokApi():
  def __init__(self) -> None:
    self.tiktok_api_url = 'https://www.tiktok.com/api'
    self.headers = {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

  def get_user_followers(
    self,
    secUid: str,
    minCursor: int = 0,
    maxCursor: int = 0,
    count: int = 50
  ):
    
    url = f'{self.tiktok_api_url}/user/list/'
    params = {
      'secUid': secUid,
      'count': count,
      'minCursor': minCursor,
      'maxCursor': maxCursor,
      'scene': 67
    }

    try:
      res = requests.get(url, params, headers=self.headers)

      if res.status_code != 200:
        print(f'Status Code: {res.status_code}')
        return None
      
      res_json = res.json()
      
      minCursor = res_json.get('minCursor')
      maxCursor = res_json.get('maxCursor')
      followers = res_json.get('userList')
      print(f'minCursor: {minCursor} - maxCursor: {maxCursor}')

      if not followers or len(followers) == 0:
        return None
      
      results = []
      for follower in followers:
        userStats = follower.get('stats')
        userInfo = follower.get('user')
        
        results.append({
          # Info
          'id': userInfo.get('id'),
          'secUid': userInfo.get('secUid'),
          'uniqueId': userInfo.get('uniqueId'),
          'nickname': userInfo.get('nickname'),
          'bio': userInfo.get('signature'),
          'avatar': userInfo.get('avatarLarger'),
          'verified': userInfo.get('verified'),
          # Stats
          'diggCount': userStats.get('diggCount'),
          'followerCount': userStats.get('followerCount'),
          'followingCount': userStats.get('followingCount'),
          'heartCount': userStats.get('heartCount'),
          'videoCount': userStats.get('videoCount'),
        })

      return {
        'minCursor': minCursor,
        'maxCursor': maxCursor,
        'followers': results
      }
    except Exception as err:
      print(err)
      return None

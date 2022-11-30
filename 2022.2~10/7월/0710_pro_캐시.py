from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    # 아래 코드로 했다면 26번 조건 필요 없음
    # cache = deque(maxlen=cacheSize)
    
    for i in cities:
        # 대소문자 구분 없으니 모두 대문자로
        i = i.upper()
        
        # 도시가 이미 있다면 chche hit -> 1초
        if i in cache:
            answer += 1
            # 원래 있던 거를 맨 뒤로 보내기
            cache.remove(i)
            cache.append(i)
            
        # 도시가 존재하지 않는 다면 cache miss -> 5초
        else:
            answer += 5
            # 추가
            cache.append(i)
            # 캐시 크기보다 크다면 제일 먼저 넣은 거 삭제
            if len(cache) > cacheSize:
                cache.popleft()
                
    return answer
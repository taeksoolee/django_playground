[참고]https://leffept.tistory.com/330

## docker command

### Image
``` shell
docker images # 이미지 목록 보기
docker search [image_name] # 이미지 검색
docker pull [image_name]:[version] # 이미지 받기
docker rmi [image_id] # 이미지 삭제
```

### Container
``` shell
docker ps
docker run [options] image[:TAG|@DIGEST] [COMMAND] [ARG...]
docker start [container_id or name]
docker restart [container_id or name]
docker attach [container_id or name]
docker stop [container_id or name]
coekr rm [container_id or name]
```

### Build
``` shell
# (Dockerfile이 위치한 디렉토리에서 실행하여) 이미지 생성
docker build -t [image_name] .
```
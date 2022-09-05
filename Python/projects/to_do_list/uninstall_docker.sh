docker rm todolist
docker rmi bervo/todolist:latest
if [ "$1" = "vol" ]
then
    echo "**************************unused volumes and data will be deleted! ****************************"
    docker volume prune
    sudo rm -dr $(pwd)/data
fi
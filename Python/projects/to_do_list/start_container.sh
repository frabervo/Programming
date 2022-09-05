docker build -t bervo/todolist .
docker run -it -v $(pwd)/data:/root/.todolists --name todolist bervo/todolist
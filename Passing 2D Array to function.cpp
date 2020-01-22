#include<iostream>
using namespace std;

void MicroAndMaze(int* maze, int N, int M){
  for(int i=0; i<N; i++){
    for(int j=0; j<M; j++){
      cout<<*(maze+i*M+j)<<" ";
    }
  }
}

int main(){
  int N, M;
  N = 3;
  M = 3;
  int maze[N][M];

  for(int i=0; i<N; i++){
    for(int j=0; j<M; j++){
      cin>>maze[i][j];
    }
  }

  MicroAndMaze((int*)maze, N, M);
  return 0;
}

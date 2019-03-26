package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
    "log"
    "math"
    //"sort"
)

func atoi(str string) int{
  a,err := strconv.Atoi(str)
  if err != nil{
    fmt.Println("aa")
    log.Fatal(err)
    os.Exit(1)
  }
  return a
}

func main() {

    var sc = bufio.NewScanner(os.Stdin)
    sc.Split(bufio.ScanWords)
    
    sc.Scan()
    N:= atoi(sc.Text())

    z := [100][2]int{}
  
    for i:=0; i<N; i++{
      sc.Scan()
      z[i][0]= atoi(sc.Text())
      sc.Scan()
      z[i][1]= atoi(sc.Text())
    }
  
  length :=0.0
   
  for i:=0; i<N; i++{
    for j:=i; j<N; j++{
      if math.Pow(float64(z[i][0] - z[j][0]),2.0) + math.Pow(float64(z[i][1] - z[j][1]),2.0) > length{
        length = math.Pow(float64(z[i][0] - z[j][0]),2.0) + math.Pow(float64(z[i][1] - z[j][1]),2.0)
      }
    }
  }
  fmt.Println(math.Pow(length, 0.5))
}
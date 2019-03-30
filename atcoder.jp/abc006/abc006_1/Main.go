package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
)

var sc = bufio.NewScanner(os.Stdin)

func nextInt() int {
    if !sc.Scan(){
      os.Exit(1)
    }
    i, e := strconv.Atoi(sc.Text())
    if e != nil {
        panic(e)
    }
    return i
}

func main() {

    sc.Split(bufio.ScanWords)
    a :=nextInt();
    if a%3 == 0{
      fmt.Println("YES")
    }else{
      fmt.Println("NO")
    }
}

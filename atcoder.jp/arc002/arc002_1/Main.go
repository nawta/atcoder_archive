package main

import (
    "fmt"
    "os"
)

func main() {
    var y int
    judge:=0
    fmt.Fscan(os.Stdin, &y)

    if y%4 == 0{
      judge++
         // fmt.Println(judge)
      if y%100==0{
        judge++
           // fmt.Println(judge)
        if y%400==0{
          judge++
             // fmt.Println(judge)
        }
      }
    }
   // fmt.Println(judge)
   if judge%2 !=0{
    fmt.Println("YES")
  }else{
    fmt.Println("NO")
  }
}
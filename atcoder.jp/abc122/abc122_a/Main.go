package main
 
import (
  "fmt"
  "os"
)
 
func main() {
  var b string
  fmt.Scan(&b)
  //fmt.Fscan(os.Stdin, &b)
  
  switch b{
    case "A":
    fmt.Print("T")
    case "T":
    fmt.Println("A")
    case "G":
    fmt.Fprintln(os.Stdout, "C")
    case "C":
    c := fmt.Sprint("G")
    fmt.Print(c) 
  }
}
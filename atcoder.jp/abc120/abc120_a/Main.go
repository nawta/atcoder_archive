package main

import(
  "fmt"
  "bufio"
  "os"
  "strconv"
)

func main(){
  var a, b, c int
  var e error
  var sc = bufio.NewScanner(os.Stdin)
  sc.Split(bufio.ScanWords) //スペースでトークンを分けるようになってる
  
  if sc.Scan(){
  	a, e = strconv.Atoi(sc.Text())
    if e != nil {
        panic(e)
    }
  }
  if sc.Scan(){
  	b, e = strconv.Atoi(sc.Text())
    if e != nil {
        panic(e)
    }
  }
  if sc.Scan(){
  	c, e = strconv.Atoi(sc.Text())
    if e != nil {
        panic(e)
    }
  }

  
  if a*c <= b{
    fmt.Printf("%d", c)
  }else{ //elseの前に改行入れたら怒られる
    fmt.Printf("%d", b/a)
  }
}
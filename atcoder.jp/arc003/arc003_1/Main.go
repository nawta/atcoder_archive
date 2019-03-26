package main

import (
    "fmt"
    "strings"
)

func main() {
    var N float64
    var s string
    fmt.Scan(&N)
    fmt.Scan(&s)

    fmt.Println(float64(strings.Count(s, "A")*4+strings.Count(s, "B")*3+strings.Count(s, "C")*2+strings.Count(s, "D"))/N)
  return //キャスト使える…？ただ、型が一致していないorメモリ使用ビット数が一致してないと弾かれる(float64とfloat32とか)
}
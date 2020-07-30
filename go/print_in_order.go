package main

import (
    "fmt"
    "sync"
)

type Foo struct {
    mtxA, mtxB, mtxC *sync.Mutex
}

func buildFoo () Foo {
    mtxA := sync.Mutex{}
    mtxB := sync.Mutex{}
    mtxC := sync.Mutex{}
    mtxB.Lock()
    mtxC.Lock()
    return Foo{&mtxA, &mtxB, &mtxC}
}

func (f Foo) sendA(ch chan string) {
    f.mtxA.Lock()
    ch <- "A"
    f.mtxB.Unlock()
} 

func (f Foo) sendB(ch chan string) {
    f.mtxB.Lock()
    ch <- "B"
    f.mtxC.Unlock()
}

func (f Foo) sendC(ch chan string) {
    f.mtxC.Lock()
    ch <- "C"
}

func main() {
    ch := make(chan string)
    foo := buildFoo()
    go foo.sendA(ch)
    go foo.sendB(ch)
    go foo.sendC(ch)

    for i := 0; i < 3; i++ {
        fmt.Println(<-ch)
    }
}
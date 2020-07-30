package main

import (
	"fmt"
	"sync"
)

type FooBar struct {
	mtxFoo *sync.Mutex
	mtxBar *sync.Mutex
}

func newFooBar() FooBar {
	mtxFoo, mtxBar := sync.Mutex{}, sync.Mutex{}
	mtxBar.Lock()
	return FooBar{&mtxFoo, &mtxBar}
}

func (fb FooBar) sendFoo(ch chan string) {
	for i := 0; i < 5; i++ {
		fb.mtxFoo.Lock()
		ch <- "Foo"
		fb.mtxBar.Unlock()
	}
}

func (fb FooBar) sendBar(ch chan string) {
	for i := 0; i < 5; i++ {
		fb.mtxBar.Lock()
		ch <- "Bar"
		fb.mtxFoo.Unlock()
	}
}

func main() {
	fooBar := newFooBar()
	ch := make(chan string)
	go fooBar.sendFoo(ch)
	go fooBar.sendBar(ch)

	for i := 0; i < 10; i++ {
		fmt.Println(<-ch)
	}
}

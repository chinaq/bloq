# Promise in JS

### 如题
```js
(function test() {
    setTimeout(function() {console.log(4)}, 0);
    new Promise(function executor(resolve) {
        console.log(1);
        for( var i=0 ; i<10000 ; i++ ) {
            i == 9999 && resolve();
        }
        console.log(2);
    }).then(function() {
        console.log(5);
    });
    console.log(3);
})()

// outputs: 1,2,3,5,4
```

* 当前task运行，执行代码。首先`setTimeout`的callback被添加到tasks queue中；
* 实例化promise，输出 `1`; promise resolved；输出 `2`;
* `promise.then`的callback被添加到microtasks queue中；
* 输出 `3`;
* 已到当前task的end，执行microtasks，输出 `5`;
* 执行下一个task，输出`4`。




### 再解
- 为了让第2，3步更清晰一点，可以写成下面这样。

```js
// 1
setTimeout();
// 2
var promise = new Promise(executor);
// 3
promise.then(callback)
// 4
console.log(3)
```

- 其中，得到`Promise`的实例promise的时候，`exectuor`作为参数传给`Promise`的构造函数同步执行。所以输出了数字`1`和`2`。
- 构造函数执行完后，我们得到了`promise`（它是`resolved`）。
- 调用`promise.then`，`callback`被添加到microtasks的队列中。
- `console.log(3)`执行完后，当前执行栈为空，则开始执行microtasks。

## ref
- [从Promise来看JavaScript中的Event Loop、Tasks和Microtasks](https://github.com/creeperyang/blog/issues/21)
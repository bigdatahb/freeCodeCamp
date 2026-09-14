# JavaScript

学习笔记参考 https://gitee.com/jsmass/study-notes/tree/master/languages/javaScript/eloquent_javaScript

## JavaScript Fundamentals

### Variables and Strings

#### 基本数据类型和变量

JavaScript 有 8 种数据类型，7 种基本数据类型（存储在栈中，不可变）和一种复杂数据类型 `object`

- number 包括整数和小数，特殊值有 `NaN` 和 `Infinity`

- string 文本字符串，使用 UTF-16 编码
    - 字符串可以用单引号、双引号和反引号来表示，使用反引号的字符串也叫做 **模板字面量**

    - 字符串拼接可以使用 `+`, 也可以使用 `concat()` 函数: `s1.concat(s2, s3, ...)`

- boolean 只有 `true` 和 `false` 两个值
    - 在 JavaScript 中有 5 种 falsy value: `0`, `''`, `undefined`, `null`, `NaN`

- null 该类型也只有一个值，那就是字面值 `null` ，它是一个空指针对象，需要注意的是 `typeof null` 会误判成 `object` （著名 bug）

- undefined 声明未赋值的变量，默认值就是 `undefined`

- symbol （ES6 新增） 该数据类型的主要用途是 **确保对象属性使用唯一标识符**。它可以创建唯一标识号

- bigint （ES2020 新增）

- object

> 使用 `typeof` 可以查看变量的数据类型

javaScript 是弱类型语言, 定义变量无需指定数据类型, 只需要使用限定符即可. 有 3 种限定符: `var`, `let`, `const`

使用指南: `var` 是 ES2015 以前版本的遗留物, 在 modern javaScript 中应避免使用.

<figure>
<blockquote cite="https://eloquentjavascript.net/02_program_structure.html">

**JavaScript 提供了一种称为绑定（或变量）的功能(binding or variable)**

你应该把绑定想象成 **触手** 而不是盒子, 他们不存储值, 而是抓住值(引用), 两个绑定可以指向同一个值

对于没有赋予任何值的绑定, 使用它将会得到一个 `undefined`

可以使用 `let`, `const`, `var` 来定义绑定(变量)

</blockquote>
<figcaption><cite>Eloquent JavaScript fourth edition - Marijn Haverbeke</cite></figcaption>
</figure>

JavaScript 中，变量名只能包含字母、数字、下划线和美元符号，不能以数字开头。变量名区分大小写

命名规范：

- 使用小驼峰命名

- 不能使用 JavaScript 关键字命名变量

- 变量名应该具有描述性意义

#### 字符串

JavaScript 可以使用 `''` 或 `""` 来表示字符串，在字符串中使用特殊字符需要转义，这是常识。

- **字符串拼接**

    字符串可以使用 `+` 进行拼接，也可以使用 `string.concat()` 函数来拼接字符串，例如将 `s1, s2, s3` 进行拼接：

    ```js
    let s1 = 'abc';
    const s2 = 'ABC';
    const s3 = 'xyz';

    // concat 函数拼接字符串的结果会生成一个新的字符串对象，而不是将 s2, s3 拼接到 s1 中，记住字符串是不可变类型
    // 使用新字符串对 s1 重新赋值
    s1 = s1.concat(s2, s3);

    console.log(s1, s2, s3);
    ```

- **字符串插值语法**

    JavaScript 支持 **字符串插值语法**，通过 **字符串模板** 来实现，使用 `` 来表示字符串模板：

    ```js
    const name = 'Alex';
    let age = 18;

    // 使用 `` 来创建字符串模板，在字符串模板中可以使用 ${} 语法来进行插值，大括号中可以是 JavaScript 变量或者表达式
    const greeting = `Hello, my name is ${name}, ${age} years old now.`;

    console.log(greeting);
    ```

- **获取字符串中的字符**

    可以使用 `[]` 语法来获取字符串中的字符，下标从 0 开始

    ```js
    const s = 'Alex love Cindy';

    console.log(s[0]); // 获取第一个字符
    console.log(s[s.length - 1]); // 获取最后一个字符
    ```

- **获取指定字符在字符串中的位置**

    ```js
    const s = 'Alex love Cindy !';

    console.log(s.indexOf('e')); // 获取 e 在字符串 s 中第一次出现的位置： 2

    // 可以指定第二个参数，从指定位置开始查找
    console.log(s.indexOf('e', 3)); // 8

    console.log(s.indexOf('ve')); // 也可以查找子串的位置：7

    console.log(s.indexOf('Love')); // 若找不到，返回 -1
    ```

- **判断一个字符串是否包含指定子串**

    前面介绍的 `indexOf()` 方法也可以用来判断字符串是否包含指定子串，但如果只是进行判断，不需要考虑子串的位置，则还可以使用 `includes()` 方法

    `includes()` 方法的使用和 `indexOf()` 方法一样，基本语法：

    ```js
    string.includes(searchValue, (startIndex = 0)); // startIndex 参数可以省略，默认值是 0
    ```

    返回值是 `true` 或 `false`

    `indexOf()` 和 `includes()` 都是严格区分大小写的

#### 字符串切片

JavaScript 提供了一个 `slice()` 方法用于做字符串切片，返回一个新的字符串对象

基本语法如下：

```js
// 接受 2 个参数：开始索引和结束索引，注意提取结果不包含结束索引位置的字符，如果不提供 endIndex，那么将提取到字符串末尾
string.slice(startIndex, endIndex);
```

代码示例：

```js
let message = 'Hello, world!';
let greeting = message.slice(0, 5);
console.log(greeting); // Hello

let world = message.slice(7);
console.log(world); // world!
```

可以使用 **负数** 作为索引值，表示从字符串末尾倒数的位置：

```js
let message = 'JavaScript is fun!';
let lastWord = message.slice(-4); // 从倒数第 4 个位置的字符开始, -1 表示最后一个字符的位置

console.log(lastWord); // fun!
```

#### 格式化字符串

- **大小写转换**

    使用 `toUpperCase()` 和 `toLowerCase()` 方法可以进行字符串的大小写转换
    - `toUpperCase()` 将字符串所有字符转换成大写形式，原字符串不变，返回一个新的字符串对象

        ```js
        let greeting = 'Hello, World!';
        let uppercaseGreeting = greeting.toUpperCase();
        console.log(uppercaseGreeting); // "HELLO, WORLD!"
        ```

    - `toLowerCase()` 方法将字符串所有字符转换成小写
        ```js
        let shout = 'I AM LEARNING JAVASCRIPT!';
        let lowercaseShout = shout.toLowerCase();
        console.log(lowercaseShout); // "i am learning javascript!"
        ```

- **删除字符串中的空白字符**

    删除字符串开头和结尾的空白字符是一个常见的需求，JavaScript 提供了 `trim()`， `trimStart()`， `trimEnd()` 方法用来删除字符串开头或结尾的空白字符

#### 字符串替换

JavaScript 中的 `replace()` 方法允许你在字符串中查找指定的值（例如单词或字符），并将其替换为另一个值。

**谨记** JavaScript 中的字符串是不可变的！ 因此所有操作字符串相关的函数返回的都是一个新的字符串对象

```js
// searchValue 是想要替换掉的目标值，可以是字符串，也可以是正则表达式
// newValue 是准备替换 searchValue 的字符串值
string.replace(searchValue, newValue);
```

代码示例：

```js
let text = 'I love JavaScript!';
console.log(text); // "I love JavaScript!"
let newText = text.replace('JavaScript', 'coding');
console.log(newText); // "I love coding!"
```

注意事项：

- `replace()` 方法是大小写敏感的

- 默认情况下， `replace()` 方法只会替换 searchValue 的 **第一个匹配项**

- 如果想要替换所有的 searchValue, 请使用 `replaceAll()` 方法

#### 字符串重复

`repeat()` 方法是 JavaScript 中的一个内置函数，它允许你将一个字符串重复执行指定的次数。

基本语法：

```js
string.repeat(count);
```

count 是要重复的次数，需要注意的是：

- count 必须是非负数，如果传递负数，将抛出 `RangeError` 错误

- count 必须为有限值，如果传递 `Infinity` 将抛出 `RangeError` 错误

- 如果传递的是一个小数，将 **向下取整**

- 如果将 count 设置为 `0`，返回一个空字符串

#### ASCII 码和 charCodeAt() 与 fromCharCode()

**ASCII（American Standard Code for Information Interchange，美国信息交换标准代码）**，使用一个字节表示一个字符，能表示 128 个字符，范围： `0 - 127`，意味着最高位固定是 0

我国的 **国标码** 最开始就是复用了 ASCII 码的设计，最高位固定为 0，但我们的国标码使用 2 个字节表示一个汉字，这就造成了无法与 ASCII 码进行区分的历史遗留问题（到底是 2 个 ASCII 码还是 1 个国标码，无法区分）

常用的国标码有 GB2312、GBK、GB18030，不过这些都是改进的国标码，叫做 **机内码**，它将国标码每个字节的最高位设置为 1。即 `机内码 = 国标码 + 8080H`

- GB2312 是中文信息处理的基石，解决了汉字在计算机中的基本表示问题。可以表示 6,763 个汉字，682个符号，但 **无法表示繁体字和许多生僻字**，编码方式是双字节定长

- GBK 在完全保留 GB2312 编码的基础上，利用其未使用的编码空间，将汉字数量大幅扩充至 21,003 个，并 **加入了对繁体字的支持**。不过，GBK 始终只是一个技术规范，并非正式的国家标准，但因其在 Windows 系统中的广泛内置（代码页 936），成为了事实上的行业标准。编码方式采用双字节定长。

- GB18030 **是当前中国最新的强制性中文编码国家标准**，支持全部 Unicode 码位，现在可以支持 8 万多汉字及部首，采用多字节变长的方式进行编码，涵盖少数民族文字、生僻字、表情符号等。

JavaScript 字符串内部使用 UTF-16 编码（Unicode编码），ASCII 值对应于 Unicode 的前 128 个字符，关于 UTF-16 编码可以参考 [Unicode笔记](https://gitee.com/jsmass/study-notes/blob/master/languages/Java/corejava/%E5%9F%BA%E7%A1%80%E7%AF%87/01_%E5%9F%BA%E6%9C%AC%E7%A8%8B%E5%BA%8F%E7%BB%93%E6%9E%84.md#unicode)

- `charCodeAt()` 方法可以访问字符对应的代码值，也叫做 **码点**

    ```js
    let letter = 'A';
    console.log(letter.charCodeAt(0)); // 65

    let symbol = '!';
    console.log(symbol.charCodeAt(0)); // 33
    ```

- `fromCharCode()` 则执行和 `charCodeAt()` 相反的操作，即获取码值对应的字符

    ```js
    let char = String.fromCharCode(65);
    console.log(char); //  A

    let char = String.fromCharCode(97);
    console.log(char); // a

    const e = '®';
    console.log(e.charCodeAt(0));
    console.log(String.fromCharCode(174));

    let c = String.fromCharCode(0x1d546);
    console.log(c);
    ```

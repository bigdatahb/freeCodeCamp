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

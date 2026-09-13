# JavaScript

学习笔记参考 https://gitee.com/jsmass/study-notes/tree/master/languages/javaScript/eloquent_javaScript

## JavaScript Fundamentals

### Variables and Strings

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

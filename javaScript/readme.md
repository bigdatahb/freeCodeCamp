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

#### 以指定字符串开头或结尾

JavaScript 提供了两个字符串方法来判断字符串是否以指定字符串开头或结尾：

- `string.startsWith(value)`

- `string.endsWith(value)`

#### 字符串分割

`split()` 方法可以对字符串进行分割，返回一个字符串数组，基本语法：

```js
string.split(splitter);
```

常见的分隔符类型：

- `""` 空字符串，它会将字符串拆分为单个字符的数组

- `" "` 空格，以空格为分隔符对字符串进行分割

- `"-"`，以短杠为分隔符对字符串进行分割

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

### Numbers and Booleans

#### Number

JavaScript 中所有数值都是 `number` 类型，包括两个特殊值： `NaN` 和 `Infinity`

可以使用 `typeof` 运算符查看对象的数据类型

JavaScript 支持的数值字面量除了 10 进制，还支持二进制、八进制、十六进制：

```js
const a1 = 10;
const a2 = 0xa; // 16进制, 使用前缀 0x
const b = 0017; // 八进制, 使用前缀 0o 或者 00 , 15
const x = 0b01011111; // 二进制字面量, 使用前缀 0b , 95
console.log(`a1=${a1}, a2=${a2}, b = ${b}, x = ${x}`);
```

#### 算术运算符

`+`， `-`， `*`， `/`， `%`， `**`

需要注意的是尝试除以 0 会返回 `Infinity`

#### 字符串与数值进行运算

当字符串与数值进行加、减、乘、除运算的时候，JavaScript 会尝试对某一个操作数进行强制类型转换，如果转换之后运算不成功则返回 NaN

```js
const result = 5 + '10';

console.log(result); // 510
console.log(typeof result); // string

const subtractionResult = '10' - 5;
console.log(subtractionResult); // 5
console.log(typeof subtractionResult); // number

const multiplicationResult = '10' * 2;
console.log(multiplicationResult); // 20
console.log(typeof multiplicationResult); // number

const divisionResult = '20' / 2;
console.log(divisionResult); // 10
console.log(typeof divisionResult); // number

const subtractionResult = 'abc' - 5;
console.log(subtractionResult); // NaN
console.log(typeof subtractionResult); // number

const multiplicationResult = 'abc' * 2;
console.log(multiplicationResult); // NaN
console.log(typeof multiplicationResult); // number

const divisionResult = 'abc' / 2;
console.log(divisionResult); // NaN
console.log(typeof divisionResult); // number
```

#### 布尔值的算术运算

JavaScript 在数学运算中将布尔值视为数字： `true` 变为 1 ， `false` 变为 0 。

```js
const result1 = true + 1;
console.log(result1); // 2
console.log(typeof result1); // number

const result2 = false + 1;
console.log(result2); // 1
console.log(typeof result2); // number

const result3 = 'Hello' + true; // 将布尔值转为字符串
console.log(result3); // "Hellotrue"
console.log(typeof result3); // string
```

#### null 和 undefined 的算术运算

在算术运算中，JavaScript 将 `null` 作为 0， 将 `undefined` 作为 NaN

```js
const result1 = null + 5;
console.log(result1); // 5
console.log(typeof result1); // number

const result2 = undefined + 5;
console.log(result2); // NaN
console.log(typeof result2); // number
```

JavaScript 经常执行类型强制转换，自动转换诸如数字、字符串和布尔值等数据类型，有时转换方式可能出乎意料。理解这些转换对于避免项目中的错误和编写健壮的代码至关重要。

#### Boolean

可以使用 `Boolean()` 来检查值的真假

常见的 `false` 值：

- 空字符串

- 0

- null

- undefined

- NaN

#### 一元运算符

- `+` 和 `-` 既可以是二元运算符（加、减），也可以是一元运算符（正、负）：

    ```js
    const str = '42';
    const strToNum = +str;

    console.log(strToNum); // 42
    console.log(typeof str); // string
    console.log(typeof strToNum); // number

    const s = '42';
    const strToNegativeNum = -s;

    console.log(strToNegativeNum); // -42
    console.log(typeof s); // string
    console.log(typeof strToNegativeNum); // number
    ```

- 逻辑非运算符 `!`

    true 变 false, false 变 true

- 按位取反运算符 `~`

- `void` 运算符

    它会计算一个表达式并返回 `undefined`

    ```js
    const result = void (2 + 2);

    console.log(result); // undefined
    ```

    `void` 也常用于超链接中，禁止导航:

    ```html
    <a href="javascript:void(0);">Click Me</a>
    ```

- `typeof` 运算符

    返回操作数的类型，以字符串形式表示。

    ```js
    const value = 'Hello world';

    console.log(typeof value); // string
    ```

#### 位运算

常见的位运算类型：

- 按位与 `&`

- 按位或 `|`

- 按位非 `~`

- 异或 `^`

- 右移 `>>`

- 左移 `<<`

#### 三元运算符

`? :`

#### 二元逻辑运算符

- `&&`

    逻辑与，检查两个操作数是否都为真，并返回结果。如果两个操作数都为真，则返回第二个值，即右侧的值:

    ```js
    const result = true && 'hello';

    console.log(result); // hello
    ```

    如果其中一个操作数为假，则返回该假值：

    ```js
    const result = 0 && 3;

    console.log(result); // 0
    ```

    如果两个操作数都为假值，则返回第一个假值：

    ```js
    const result = false && 0;

    console.log(result); // false
    ```

- `||`

    逻辑或，检查两个操作数中是否至少有一个为真。如果第一个操作数为真，则返回该值：

    ```js
    const result = 'This is truthy' || false;

    console.log(result); // This is truthy
    ```

    如果第一个操作数为假，而第二个操作数为真，则返回第二个值：

    ```js
    const result = 0 || 'This is truthy';

    console.log(result); // This is truthy
    ```

- `??`

    空值合并运算符，仅当第一个值是 `null` 或 `undefined` 时才返回第二个值

    ```js
    const result = null ?? 'default';

    console.log(result); // default

    const userSettings = {
        theme: null,
        volume: 0,
        notifications: false,
    };

    let theme = userSettings.theme ?? 'light';
    console.log(theme); // light
    ```

#### Math 对象及常用方法

JavaScript 内置了一个 `Math` 对象来提供一些简单的数学运算

主要方法有：

- `Math.random()`， 生成一个介于 0（包含）到 1（不包含）之间的随机小数

- `Math.min()` 和 `Math.max()`，返回一组数中的最小值和最大值

- `Math.round()`，四舍五入返回最近的一个整数

- `Math.floor()` 和 `Math.ceil()`
    - `Math.floor()` 向下取整

    - `Math.ceil()` 向上取整

    生成两个整数之间的随机数：

    ```js
    // 随机生成 [5, 10] 之间的整数
    const max = 10;
    const min = 5;
    const randomNum = Math.floor(Math.random() * (max - min + 1)) + min;
    console.log(randomNum);
    ```

- `Math.trunc()`，移除数值的小数部分，只返回整数部分

    ```js
    console.log(Math.trunc(2.9)); // 2
    console.log(Math.trunc(9.1)); // 9
    ```

- `Math.sqrt()` 和 `Math.cbrt()`，求平方根和立方根

    ```js
    console.log(Math.sqrt(81)); // 9
    console.log(Math.cbrt(27)); // 3
    ```

- `Math.abs()`，求绝对值

- `Math.pow(a, b)` 求 a 的 b 次方

#### isNaN()

在 JavaScript 中， `NaN` 是一个特殊值，表示无法表示的或者未定义的一个数值结果

我们要判断一个值是不是 `NaN` 不能使用比较运算符 `==` 或 `===`，`NaN` 不等于任何值，包括它自身：

```js
console.log(NaN === NaN); // false
```

我们要判断一个值是否是 `NaN` 可以使用 JavaScript 的 `isNaN()` 函数：

```js
console.log(isNaN(NaN)); // true
console.log(isNaN(undefined)); // true
console.log(isNaN({})); // true

console.log(isNaN(true)); // false
console.log(isNaN(null)); // false
console.log(isNaN(37)); // false

console.log(isNaN('37')); // false: "37" is converted to 37
console.log(isNaN('37.37')); // false: "37.37" is converted to 37.37
console.log(isNaN('')); // false: empty string is converted to 0
console.log(isNaN(' ')); // false: string with a space is converted to 0

console.log(isNaN('blabla')); // true: "blabla" is not a number
```

`isNaN()` 函数首先尝试将参数转换为数字。如果无法转换，则返回 `true`，这种行为可能会导致一些意想不到的结果，尤其是在处理可以强制转换为数字的字符串时。

由于这些潜在的不一致性，ES6（JavaScript 第六版，于 2015 年发布）引入了 `Number.isNaN()` 方法

#### Number.isNaN()

该方法不会在测试前尝试将参数转换为数字。它仅当值恰好为 `NaN` 时才返回 `true`

```js
console.log(Number.isNaN(NaN)); // true
console.log(Number.isNaN(Number.NaN)); // true
console.log(Number.isNaN(0 / 0)); // true

console.log(Number.isNaN('NaN')); // false
console.log(Number.isNaN(undefined)); // false
console.log(Number.isNaN({})); // false
console.log(Number.isNaN('blabla')); // false
```

#### toFixed()

`toFixed()` 方法是 JavaScript 内置函数，用于将数字格式化为固定小数位数的 **字符串**，注意返回的是字符串

```js
let num = 3.14159;
console.log(num.toFixed(2)); // "3.14"
```

**最后一位会进行四舍五入**

如果不提供参数， `toFixed()` 会返回一个四舍五入的整数的字符串形式

### Functions

#### 定义函数的方式

定义函数的三种方式:

- **变量赋值法**

    在 `javaScript` 中, 函数本身也是一个值, 可以赋值给变量:

    ```js
    // 方式一: 将函数赋值给变量
    /*
     * 定义一个变量 square, 将一个匿名函数绑定给它
     */
    const square = function (x) {
        return x * x;
    }; // 这是一个语句, 后面加 ;
    ```

- **声明表示法**

    ```js
    // 方式二: 函数声明;
    /**
     * 声明一个函数 add
     */
    function add(a, b) {
        return a + b;
    }
    ```

    变量绑定和函数声明法定义函数的区别:
    1. **函数声明式定义** 不是自上而下的控制流, 它 **会将定义提升至其范围的顶部**, 因此声明式函数的定义可以在其范围内的任意位置. 可以先使用再定义
    2. **变量绑定式定义函数, 和变量一致, 需要先定义再使用**
    3. 变量定义需要加 `;` (虽然不加也可以, 但是会让 `javaScript engine` 去解析), 声明式函数定义后面无需加 `;`

    ```js
    // 在函数声明前使用函数，因为 future 的定义会进行提升
    console.log('The future says:', future()); // ok, 函数声明会移动到这个范围的顶部

    function future() {
        return "You'll never have flying cars";
    }

    console.log(add(1, 2)); // ReferenceError: Cannot access 'add' before initialization

    const add = function (a, b) {
        return a + b;
    };
    ```

- **箭头函数**

    不使用 `function` 关键字, 而是使用 `=>` 来定义函数

    ```js
    const roundTo = (n, step) => {
        let remainder = n % step;
        return n - remainder + (remainder < step / 2 ? 0 : step);
    };
    ```

    **箭头函数只能使用变量赋值的方式定义**, 若函数体只有一行语句, 可以省略 `{}`, 若参数只有一个, 可以省略 `()`:

    ```js
    const square = (x) => x * x; // 如果移除了 {} , 则不能显示使用 return 语句
    ```

在 JavaScript 中, 函数参数都是可选的, 如果函数参数没有指定默认值, 调用的时候也没有传递实参, 那么它的值就是 `undefined`

#### 给参数设置默认值

可以在参数列表中, 使用 `=` 给参数定义默认值

```js
// 对第二个参数 step 设置默认值
function roundTo(n, step = 1) {
    let remainder = n % step;
    return n - remainder + (remainder < step / 2 ? 0 : step);
}

console.log(roundTo(4.5));
// → 5
console.log(roundTo(4.5, 2));
// → 4
```

#### 函数返回值

函数执行完毕后，总会返回一个值。默认情况下，返回值为 `undefined`：

```js
function doSomething() {
    console.log('Doing something...');
}

let result = doSomething();
console.log(result); // undefined
```

可以使用 `return` 关键字来指定返回值

**注意**：JavaScript 的函数没有返回类型，因此同一个函数可以根据情况返回不同类型的值

#### 作用域

作用域指的是变量在代码不同部分的可见性和可访问性

在 JavaScript 中，作用域主要分为三种类型：**全局作用域（global scope）**、**局部作用域（local scope）** 和 **代码块作用域（block scope）**

- 全局作用域是 JavaScript 程序中最外层的作用域，在全局作用域中声明的变量叫做全局变量，全局变量可以在声明之后，或者函数和代码块内部进行访问

- 局部作用域是指函数内部的作用区域

- 局部作用域是指代码块作用域，是 ES6 中引入的概念， 代码块是指 `{}` 括起来的代码片段，在代码块中使用 `let`, `const` 定义的变量只能在该代码块内访问

全局变量应谨慎使用，容易产生变量名称冲突，使代码难以维护。

### Arrays

#### JavaScript 数组的特点

- 使用 `[]` 来创建数组

- JavaScript 中，数组元素可以是 **不同数据类型的值**，数组元素可以是数值、字符串、布尔值、对象或者其他数组

    ```js
    let arr = [1, 2, 'apple', true];

    console.log(arr);
    ```

- 数组元素索引从 0 开始

- JavaScript 的数组是动态的，其大小可以在创建后发生改变

    可以使用各种数组相关方法来添加或删除元素，例如 `push()`, `pop()`, `shift()`, `unshift()`, `splice()` 等

- 可以直接为超出数组长度的位置索引直接赋值

    ```js
    let arr = [1, 2, 'apple', true];

    console.log(arr);

    arr[6] = 'banana';
    console.log(arr); // [ 1, 2, 'apple', true, <2 empty items>, 'banana' ]
    ```

    **请务必要防止这种情况发生，有可能会导致意外行为！**

- 访问不存在的元素会返回 `undefined`

    例如数组总共才 5 个元素，但是我访问 `arr[10]`，不会报错，返回的是 `undefined`

- 获取数组长度使用 `length` 属性

    ```js
    const arr = [1, 2, 3, 4];
    console.log(arr.length);
    ```

#### 数组解构

类似 Python 的元组解包操作，JavaScript 为数组提供了解构操作，它是一种便捷的语法特性

```js
let fruits = ['apple', 'banana', 'orange'];

let [first, second, third] = fruits;

console.log(first); // "apple"
console.log(second); // "banana"
console.log(third); // "orange"
```

数组解构还允许你使用逗号跳过不感兴趣的元素:

```js
let colors = ['red', 'green', 'blue', 'yellow'];
let [firstColor, , thirdColor] = colors;

console.log(firstColor); // "red"
console.log(thirdColor); // "blue"
```

数组解构的另一个强大功能是能够使用 **默认值**。如果数组元素少于要赋值的变量数量，则可以提供默认值：

```js
let numbers = [1, 2];
let [a, b, c = 3] = numbers;

console.log(a); // 1
console.log(b); // 2
console.log(c); // 3
```

---

**剩余元素语法（扩展运算符）**： `...` ，它允许你捕获数组中尚未解构到新数组中的剩余元素

```js
let fruits = ['apple', 'banana', 'orange', 'mango', 'kiwi'];
let [first, second, ...rest] = fruits;

console.log(first); // "apple"
console.log(second); // "banana"
console.log(rest); // ["orange", "mango", "kiwi"]
```

剩余元素必须是数组解构模式中的最后一个元素，也就是说 **不能使用** `let [first, ...rest, last] = data;` 这样的语法

根据数组解构的剩余元素语法，我们可以很容易的复制一个数组：

```js
// 复制数组
let src = ['apple', 3, 2.98];
let copy = [...src];
```

#### 数组相关方法

- `push()` 在数组 **末尾** 添加 **一个或多个** 元素，返回数组的新长度

- `unshift()` 在数组的 **头部** 添加 **一个或多个** 元素，返回数组的新长度

- `pop()` 移除数组的 **最后一个** 元素，并返回该元素，数组长度减一

- `shift()` 移除数组的 **第一个** 元素，并返回该元素，数组长度减一

- `reverse()` 反转数组元素

- `join()` 将数组元素以指定分隔符进行连接

- `indexOf()` 查找指定元素在数组中的第一个位置索引，如果找不到该元素，返回 `-1`

    基本语法：

    ```js
    // fromIndex 是可选的，默认为 0
    array.indexOf(element, fromIndex);
    ```

- `splice()` 一个修改数组非常强大的工具，可以从数组的任意位置添加或删除元素，返回值是从数组中删除的元素所组成的数组，如果没有删除任何元素，则返回一个空数组。**注意**，这个方法会修改原数组
    - 基本语法：

        ```js
        // startIndex: 指定修改数组的开始索引
        // itemsToRemove: 可选参数，指定要删除的元素数量，如果省略 itemsToRemove 参数， splice() 将删除从 startIndex 开始到数组末尾的所有元素
        // 后续参数 item1, item2, ... 是要添加到数组的元素，从 startIndex 位置开始添加
        array.splice(startIndex, itemsToRemove, item1, item2);
        ```

    - 示例：

        ```js
        let colors = ['red', 'green', 'blue'];
        colors.splice(1, 0, 'yellow', 'purple');

        console.log(colors); // ["red", "yellow", "purple", "green", "blue"]

        let numbers = [1, 2, 3, 4, 5];
        numbers.splice(1, 2, 6, 7, 8);

        console.log(numbers); // [1, 6, 7, 8, 4, 5]
        ```

    - 我们可以使用下标语法来修改数组元素，比如 `arr[1] = "X";`，我们也可以通过 `splice()` 来实现元素的修改：

        ```js
        // 修改位置 1， 删除 1 个元素，然后在位置 1 添加一个元素 "X"
        arr.splice(1, 1, 'X');
        ```

    - 另一个常见用法是删除指定索引位置的元素：

        ```js
        const fruits = ['apple', 'banana', 'orange', 'mango'];
        const indexToRemove = fruits.indexOf('orange');
        if (indexToRemove !== -1) {
            // 删除 indexToRemove 处的元素
            fruits.splice(indexToRemove, 1);
        }
        ```

    - 清空数组

        ```js
        // 省略 itemsToRemove 参数，splice() 将删除从 startIndex 开始到数组末尾的所有元素
        let array = [1, 2, 3, 4, 5];
        array.splice(0);

        console.log(array); // []
        ```

- `includes()` 检查数组是否包含某个特定值，返回一个布尔值

    与字符串的 `includes()` 一样，如果只想知道是否包含，而不需要位置信息可以使用这个方法

    基本语法：

    ```js
    // fromIndex 是可选参数，默认值为 0
    array.includes(value, fromIndex);
    ```

#### 数组浅拷贝

浅拷贝是指将基本类型数据进行拷贝，对于引用类型则只拷贝引用值

创建数组浅拷贝的方法有很多种，我们将探讨其中最常用的一些方法： `concat()` ， `slice()` 和 扩展运算符 `...`

- 使用 `concat()` 进行浅拷贝

    ```js
    const originalArray = [1, 2, 3];
    const copyArray = [].concat(originalArray);

    console.log(copyArray); // [1, 2, 3]
    console.log(copyArray === originalArray); // false
    ```

- 使用 `slice()` 进行浅拷贝

    `slice()` 方法本身是用来对字符串或数组进行切片的，返回切片的新数组

    ```js
    const originalArray = [1, 2, 3];
    const copyArray = originalArray.slice();

    console.log(copyArray); // [1, 2, 3]
    console.log(copyArray === originalArray); // false
    ```

- 使用 `...` 进行浅拷贝

    ```js
    const originalArray = [1, 2, 3];
    const copyArray = [...originalArray];

    console.log(copyArray); // [1, 2, 3]
    console.log(copyArray === originalArray); // false
    ```

### Objects

#### 对象的创建与属性访问

在 JavaScript 中，对象是一种基本数据结构，是一种引用类型数据

使用 `{}` 来表示对象，在对象中，以键值对的形式来定义属性：

```js
const person = {
    name: 'Alice',
    age: 30,
    city: 'New York',
};
```

可以通过 `[]` 语法来获取对象的属性值，或者是 `objectName.propertyName` 的方式获取属性值，`[]` 中可以使用 JavaScript 表达式

```js
console.log(person.name);
console.log(person['name']);
```

#### 移除对象的属性

- `delete`

    使用 `delete` 删除对象属性是最直接、最常用的方法

    ```js
    const person = {
        name: 'Alice',
        age: 30,
        job: 'Engineer',
    };

    delete person.job;

    console.log(person.job); // undefined
    ```

- 通过 **解构赋值** 创建新对象来达到删除对象属性的目的（本质上不是删除对象属性，而是创建一个不包含某些属性的新对象）

    ```js
    const person = {
        name: 'Bob',
        age: 25,
        job: 'Designer',
        city: 'New York',
    };

    // 解构赋值
    const { job, city, ...remainingProperties } = person;

    // { name: "Bob", age: 25 }
    console.log(remainingProperties);
    ```

#### 检查一个对象是否具有某个属性

- `hasOwnProperty()` 检查对象是否拥有指定的属性，返回一个布尔值

    ```js
    const person = {
        name: 'Alice',
        age: 30,
    };

    console.log(person.hasOwnProperty('name')); // true
    console.log(person.hasOwnProperty('job')); // false
    ```

- `Object.hasOwn()` 现代推荐的检查对象是否拥有自身属性（而非继承属性）的方法

    可以将其视为 `hasOwnProperty()` 的升级版，更加安全。基本语法是 `Object.hasOwn(object, propertyName)`

    ```js
    const person = {
        name: 'Alice',
        age: 30,
    };

    console.log(Object.hasOwn(person, 'name')); // true
    console.log(Object.hasOwn(person, 'job')); // false
    ```

- `in` 运算符，与 `hasOwnProperty()` 类似。返回一个布尔值

    ```js
    const person = {
        name: 'Bob',
        age: 25,
    };
    console.log('name' in person); // true
    ```

#### 原始数据类型（primitive data types)和非原始数据类型的区别

原始数据类型是 JavaScript 中最简单的数据形式。它们包括 `number`、`bigint`、`string`、`boolean`、 `null` 、 `undefined` 和 `symbol`。这些类型之所以被称为“原始”，是因为它们表示单个值，而不是对象。

**原始值是不可变的！**

当你创建一个具有非原始类型值的变量时，变量中实际存储的是对象在内存中的存储位置的引用，而不是对象本身

#### 函数和对象方法的差异

函数和对象方法都是封装可重用代码的方式，但它们在定义、使用和运行上下文方面存在一些关键差异

- 函数：

    ```js
    function greet(name) {
        return 'Hello, ' + name + '!';
    }
    console.log(greet('Alice')); // "Hello, Alice!"
    ```

- 对象方法：

    方法要通过对象才能调用

    ```js
    const person = {
        name: 'Bob',
        age: 30,
        sayHello: function () {
            // 方法中可以通过 this 关键字访问当前对象
            return 'Hello, my name is ' + this.name;
        },
    };

    console.log(person.sayHello()); // "Hello, my name is Bob"
    ```

#### JSON

JavaScript Object Notation （JSON）是一种轻量级的、基于文本的数据格式，常用于服务器和 Web 应用程序之间交换数据。

由于 JSON 与语言无关，您可以轻松地将 JSON 数据从 Java 应用程序发送到 Python 应用程序，或者从 JavaScript 应用程序发送到 C# 应用程序。

JSON 支持多种数据类型，包括 对象、数组、字符串、布尔值、null 和数字。

一个 JSON 示例：

```json
{
    "name": "Alice",
    "age": 30,
    "isStudent": false,
    "list of courses": ["Mathematics", "Physics", "Computer Science"]
}
```

访问 JSON 对象中的数据：

```js
// 从文件导入 json
import data from './example.json' with { type: 'json' };

// 1. 使用 . 访问属性
console.log(data.age);

// 2. 使用 [] 来访问属性
console.log(data['list of courses']);
```

#### JSON.parse() 和 JSON.stringify()

- `JSON.stringify()` 用于将 JavaScript 对象转换为 JSON 字符串

    ```js
    const user = {
        name: 'John',
        age: 30,
        isAdmin: true,
    };

    const jsonString = JSON.stringify(user);
    console.log(jsonString);
    ```

    `JSON.stringify()` 可以指定第二个参数（可以是一个函数或一个数组），用来指定需要进行字符串化的属性

    ```js
    const developerObj = {
        firstName: 'Jessica',
        isAwesome: true,
        isMusician: true,
        country: 'USA',
    };

    // result: {"firstName":"Jessica","country":"USA"}
    // 只对 firstName 和 country 属性进行字符串化
    console.log(JSON.stringify(developerObj, ['firstName', 'country']));
    ```

    `JSON.stringify()` 还有第三个可选参数 `spacer`，用来指定字符串化结果的间距，例如 `console.log(JSON.stringify(developerObj, null, 2));`

- `JSON.parse()` 将 JSON 字符串转换回 JavaScript 对象

    ```js
    const jsonString = '{"name":"John","age":30,"isAdmin":true}';
    const userObject = JSON.parse(jsonString);
    console.log(userObject);

    // Result:
    // { name: 'John', age: 30, isAdmin: true }
    ```

#### 可选链式运算符

可选链式运算符 `?.` 是 JavaScript 的一个实用工具，它允许你安全地访问对象属性或调用方法，而无需担心它们是否存在。

```js
const user = {
    name: 'John',
    profile: {
        email: 'john@example.com',
        address: {
            street: '123 Main St',
            city: 'Somewhere',
        },
    },
};

console.log(user?.profile?.address?.street); // "123 Main St"
console.log(user?.profile?.phone?.number); // undefined
```

通过使用可选链式运算符，我们告诉 JavaScript 仅当对象（或 `?.` 之前的值）存在且不为 `null` 或 `undefined` 时才继续执行操作

如果 `?.` 前面的值为 `null` 或者 `undefined`， JavaScript 将返回 `undefined`，而不是继续执行并抛出错误。

#### 对象解构

- 对象解构一般用法

    ```js
    const person = { name: 'Alice', age: 30, city: 'New York' };

    const { name, age } = person;

    console.log(name); // Alice
    console.log(age); // 30
    ```

- 可以将提取出的值赋给具有不同名称的变量

    ```js
    let person = { name: 'Alice', age: 30, city: 'New York' };

    let { name: personName, age: personAge } = person;

    console.log(personName); // Alice
    console.log(personAge); //  30
    ```

- 对象解构允许设置默认值

    ```js
    let person = { name: 'Alice', age: 30, city: 'New York' };
    let { name, age, country = 'Unknown' } = person;

    console.log(country); // Unknown
    ```

- 嵌套对象的解构

    ```js
    const recipe = {
        name: 'Chocolate Cake',
        ingredients: {
            flour: '2 cups',
            sugar: '1 cup',
        },
    };

    // Extract `flour` from `ingredients`
    const {
        ingredients: { flour },
    } = recipe;

    console.log(flour); // "2 cups"
    ```

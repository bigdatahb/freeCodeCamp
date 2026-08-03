# CSS

## CSS 基础

### 什么是 CSS ？

CSS 叫做层叠样式表（Cascading Style Sheets），是用来给 HTML 文档内容设置样式的

CSS 的核心功能:

- 创建响应式设计

- 样式可以被继承和覆盖（层叠一词的由来）

样式由各种 **CSS 规则** 组成， CSS 规则由两部分组成: **选择器** 和 **声明块**

CSS 规则基本语法:

```css
selector {
    property: value;
}
```

可以为多个选择器应用同一份样式，选择器之间使用逗号隔开:

```css
selector1,
selector2 {
    property: value;
}
```

### meta viewport

meta viewport 元素是响应式网页设计中的关键组件，其基本语法如下:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

这个元素通常放在 HTML 文档的 `<head>` 部分

其含义如下：

- `width=device-width` 告诉浏览器将页面宽度设置为与设备屏幕宽度相匹配

- `initial-scale=1.0` 设置页面首次加载时的初始缩放级别。值为 `1.0` 表示页面以 100% 缩放比例显示，不进行任何缩放。

通过使用 meta viewport 元素，您可以确保网页在移动设备上正确显示。

### 定义 CSS 的方式

#### 内联CSS inline css

内联 CSS 是直接在 HTML 元素中使用 `style` 属性编写的:

```html
<p style="color: green;">This is an inline-styled paragraph.</p>
```

内联 CSS 通常用于快速设置一次性样式，或覆盖特定元素的其他样式

#### 内部CSS internal css

内部 CSS 写在 HTML 文档 `head` 部分的 `style` 标签内

```html
<head>
    <style>
        p {
            color: blue;
        }
    </style>
</head>
<body>
    <p>This paragraph is styled using internal CSS.</p>
</body>
```

当您需要将样式应用于特定页面而非多个页面时，最好使用内部 CSS

#### 外部CSS external css

外部 CSS 写在单独的 `.css` 文件中，并通过 `head` 部分的 `link` 元素链接到 HTML 文档

```html
<head>
    <link rel="stylesheet" href="styles.css" />
</head>
<body>
    <p>This paragraph is styled using external CSS.</p>
</body>
```

```css
p {
    color: red;
}
```

外部 CSS 允许您对多个页面进行一致的样式设置，是专业网站开发中首选的方法

外部 CSS 非常适合希望在多个页面之间保持一致样式的大型项目，它提倡关注点分离，让 HTML 处理结构，CSS 处理样式，从而使代码更易于维护和扩展。

### width 和 height

在 CSS 中， `width` 和 `height` 属性用于控制网页上元素的尺寸。

高度和宽度可以用不同的单位定义，例如像素（ `px` ）、百分比（ `%` ）、视窗单位(viewport unit)（ `vw` 、 `vh` ）等等

`width` 和 `height` 属性如果不指定的话，默认值是 `auto`，浏览器会根据元素的内容、父元素和显示类型来确定元素的宽度和高度

对于 `div` 元素， `width: auto` 会使其扩展到填充其父容器的整个宽度。

我们还可以通过 `min-width`, `min-height` 以及 `max-width`, `max-height` 来对高度和宽度进行限制

```html
<head>
    <style>
         .box {
        <!-- 渲染宽度 150px -->
           width: 200px;
           max-width: 150px;
        <!-- 渲染高度 150px -->
           height: 200px;
           max-height: 150px;
           background-color: lightgreen;
         }
    </style>
</head>
<body>
    <div class="box"></div>
</body>
```

### CSS 组合器

CSS 组合器用于定义 CSS 选择器之间的关系，它主要通过元素之间的关系来选择元素

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width;initial-scale=1.0" />
        <title>CSS</title>
        <style>
            div p {
                color: red;
            }

            #container > span {
                color: green;
            }

            #container + p {
                color: blue;
            }

            #container ~ span {
                color: cyan;
            }
        </style>
    </head>
    <body>
        <div id="container">
            <p>container 的直接子节点</p>
            <span>直接后代选择器只选择直接子节点</span>
            <section>
                <p>container 的间接子节点</p>
                <span>后代选择器会选择所有后代</span>
            </section>
        </div>
        <p>first sibling element p of container</p>
        <span>second sibling element span of container</span>
        <p>third sibling</p>
        <span>fourth</span>
    </body>
</html>
```

- **后代组合器（descendant combinator）**

    上面代码中的 `div p` 是一个后代组合器，它选择所有 `div` 元素的所有后代节点的 `p` 元素

    在这种情况下, `div` 是父选择器， `p` 是子选择器，父子选择器之间使用 **空格分隔**

- **子组合器（child combinator）**

    也可以叫直接后代组合器，上面的 `#container > span` 就是一个子组合器，它表示选择 `#container` 元素的直接孩子节点中的 `span` 元素

- **下一个兄弟组合器（next-sibling combinator）**

    选择指定元素的下一个兄弟元素, 比如 `#container + p` 只会选择紧随 `#container` 元素之后的 `p` 元素，要保证 `#container` 后面就是 `p`（紧随）

- **后续兄弟组合器（subsequent-sibling combinator）**

    `#container ~ span` 选择的目标是所有出现在 `#container` 元素之后的兄弟节点中的 `span` 元素

**组合器也叫做复合选择器**

### inline, block, inline-block

元素主要分为 **块级元素** 和 **行内元素**， 块元素的显示方式是: `display: block;`, 行内元素是: `display: inline;`

- 块级元素会占据父容器的全部宽度，他们总是另起一行，且可以调整宽度和高度

- 行内元素只占据所需的空间，他们会融入周围的内容中，不会换行显示

其实还有第三种显示方式: `display: inline-block;`

`inline-block` 是 `inline` 和 `block` 的混合体，它在布局上和 `inline` 类似，会保持在文本流中，不会另起一行。但是，它也可以像 `block` 一样调整高度和宽度

**简而言之**: `inline` 和 `inline-block` 的主要区别在于，`inline` 元素无法控制其大小，而 `inline-block` 元素允许完全控制尺寸，同时仍与其他内容保持对齐

### margin 和 padding

margin 表示元素的外边距，即元素边框与其他元素之间的间隔

padding 表示元素的内边距，即元素内容与其边框之间的距离

`margin` 有 4 种不同的属性: `margin-top`, `margin-right`, `margin-bottom`, `margin-left`

`padding` 也有 4 种不同的属性: `padding-top`, `padding-right`, `padding-bottom`, `padding-left`

在使用的时候我们可以通过这些属性来指定各个方向上的外边距或者内边距，但是我们有简写形式，可以一次性指定一个、两个、三个或四个值

- 一个值的情况

    ```css
    p {
        /* margin-top, margin-right, margin-bottom, margin-left 的值都指定为 10px */
        margin: 10px;
    }
    ```

- 两个值的情况

    ```css
    p {
        /** 第一个值指定的是 margin-top 和 margin-bottom, 第二个值指定的是 margin-right 和 margin-left */
        margin: 10px 20px;
    }
    ```

- 三个值的情况

    ```css
    p {
        /** 第一个值是 margin-top, 第二个值指定的是 margin-right 和 margin-left, 第三个值是 margin-bottom */
        margin: 10px 20px 30px;
    }
    ```

- 四个值的情况

    ```css
    p {
        /** 4 个值分别对应 margin-top, margin-right, margin-bottom, margin-left
    		从 margin-top 开始逆时针方向
    	 */
        margin: 10px 20px 30px 40px;
    }
    ```

### CSS 优先级

CSS 优先级是一个很重要的概念，当同时有多个规则定位到同一个元素时，到底适配哪个 CSS 规则？

首先看一般的优先级规则：

- 内联样式具有最高的优先级（如果不考虑使用 `!important` 的话）

- 内部样式和外部样式具有同样的优先级

- 优先级相同的情况下，后面的会覆盖前面的

对于选择器的优先级：

- **ID 选择器 &gt; 类选择器、属性选择器、伪类 &gt; 类型选择器（标签选择器）、伪元素 &gt; 通用选择器**

优先级值的计算分为 4 个部分: (a, b, c, d)

- `a`: 内联样式 1 或 0

- `b`: ID 选择器数量

- `c`: 类选择器、属性选择器和伪类（`:hover`、`:nth-child` 等）的数量

- `d`: 类型选择器、伪元素（`::before`、`::after` 等）的数量

- 通用选择器 `*`、组合器（`+` `>` `~` `空格`）和 `:where()` 不贡献任何权重，即 (0,0,0,0)

对于如下 css 规则:

```css
div#test span {
    color: green;
}
div span {
    color: blue;
}
span {
    color: red;
}
```

`div#test span` 的优先级是 (0, 1, 0, 2)

`div span` 的优先级是 (0, 0, 0, 2)

`span` 的优先级是 (0, 0, 0, 1)

### 继承

继承是 CSS 中的一个关键概念，它决定了样式如何从父元素传递到子元素。

在 CSS 中，并非所有属性都会默认继承。例如， `color` 、 `font-family` 和 `line-height` 等属性是会继承的。

另一方面，像 `margin` 、 `padding` 、 `border` 和 `background` 这样的属性默认情况下不会被继承。如果您希望子元素继承这些样式，则需要显式地设置它们，可以直接在子元素上设置，也可以使用 **inherit** 关键字。

`inherit` 关键字可用于强制从父元素继承属性，即使该属性通常不会被继承。

```html
<div style="padding: 20px;">
    This is the parent element with padding.
    <!-- 让 p 继承 div 的 padding 属性-->
    <p style="padding: inherit;">
        This is the child element inheriting the padding.
    </p>
</div>
```

需要注意的是，**继承是单向的**，只能从父元素继承到子元素。如果您覆盖子元素的样式，则不会影响父元素。

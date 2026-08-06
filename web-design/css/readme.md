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

### 列表样式

#### 控制列表项之间的间距

我们可以通过 margin 来指定列表项之间的间距，比如给 `li` 选择器设置 `margin-bottom` 属性

有个时候也可以用 `line-height` 来间接实现列表项之间的间距

#### list-style 属性

在 CSS 中， `list-style` 属性用于控制网页上列表的外观。

`list-style` 属性实际上是其他三个属性的简写：

- `list-style-type` ，定义列表中使用的项目符号或数字的类型
    - 对于无序列表，您可以从多种项目符号样式中进行选择，例如圆点、圆形或方形。

    - 对于有序列表，您可以使用不同的编号系统，例如十进制、罗马数字，甚至字母字符。

- `list-style-position` ，控制项目符号或编号相对于列表项内容的位置。
    - 有两个值可以选择： `inside` 和 `outside`， 默认值是 `outside`

    - `outside` 表示项目符号或数字会出现在内容外部

    - `inside` 表示项目符号或数字会出现在内容内部，这可能会导致文本换行并与项目符号或数字对齐（当一个列表项的内容超过一行时，后面的行会与项目符号对齐）。

- `list-style-image`，使用图像作为列表项的符号标记

```html
<ul
    style="list-style: square inside url('https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg');"
>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>
```

### 链接样式

默认的链接样式通常用蓝色表示未访问的链接，用紫色表示已访问的链接，这已经成为用户在浏览网站时所期望和依赖的标准。

默认样式相当于：

```css
a:link {
    color: blue;
    text-decoration: underline;
}

a:visited {
    color: purple;
}
```

我们可以修改默认样式:

```css
a:link {
    color: blue;
    text-decoration: none;
    border-bottom: 1px solid blue;
}

a:visited {
    color: purple;
    border-bottom: 1px solid purple;
}
```

我们还可以给链接的其他状态设置样式:

```css
a:hover {
    color: red;
}

a:active {
    color: darkorange;
}
```

链接的状态有:

- `link` 尚未访问的链接

- `visited` 已访问或点击过的链接

- `hover` 鼠标悬停在链接上时

- `focus` 链接获得焦点时

- `active` 链接被点击时

这些状态可以使用 CSS 中的 `pseudo-classes` （伪类）来设置样式。

伪类是添加到选择器中的一个关键字，用于指定所选元素的特殊状态。

伪类语法大致如下：

```css
/** A 是选择器, :B 是伪类 */
A:b {
    property: value;
}
```

**请注意**: 这 5 个伪类如果作用于同一个链接（`<a>` 标签），必须遵循 **LVFHA** 顺序:

```css
a:link {
    color: blue;
}

a:visited {
    color: purple;
}

a:focus {
    outline: 2px solid orange;
}

a:hover {
    color: red;
}

a:active {
    color: green;
}
```

**核心原因**: CSS 层叠规则（优先级相同的情况下，后定义的覆盖先定义的）。这 5 个伪类的优先级（特异性）完全相同，所以书写在后面的样式会覆盖前面的。

### 背景图片

在 CSS 中使用背景图像时，您可以使用多个属性来控制这些图像的显示方式。

比较重要的几个属性是: `background-size`, `background-repeat`, `background-position` 和 `background-attachment`

我们先来看一下 `background-image` 属性:

```css
body {
    background-image: url('https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg');
}
```

- `background-size`
    - `contain`

        你可以使用 `contain` 将图片放大到尽可能大，而不会裁剪或拉伸：

        ```css
        body {
            background-image: url('https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg');
            background-size: contain;
            min-height: 100px;
        }
        ```

    - `cover`

        使用 `cover` 值，那么背景图像就会缩放以覆盖整个 body 元素，同时保持其宽高比

        ```css
        body {
            background-image: url('https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg');
            background-size: cover;
            min-height: 100px;
        }
        ```

        默认情况下，背景图片会在水平和垂直方向上重复排列，以填充整个父容器。不过，您可以通过 `background-repeat` 控制此行为。

- `background-repeat`
    - 图像不重复显示

        ```css
        body {
            background-image: url('https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg');
            background-size: contain;
            background-repeat: no-repeat;
            min-height: 100px;
        }
        ```

    - 图像水平方向重复

        将 `background-repeat` 的值设置为 `repeat-x` 即可实现水平重复

        ```css
        body {
            background-image: url('https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg');
            background-size: contain;
            background-repeat: repeat-x;
            min-height: 100px;
        }
        ```

    - 图像垂直方向重复

        将 `background-repeat` 的值设置为 `repeat-y` 即可实现垂直重复

- `background-position`

    要将背景图像定位到屏幕上，可以使用 `background-position` 属性。

    `background-position` 属性允许您设置背景图像在元素中的显示位置。您可以使用 `top` 、 `bottom` 、 `left` 、 `right` 和 `center` 等关键字，也可以使用特定的像素值或百分比值。

    ```css
    body {
        background-image: url('https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg');
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center top; /** 水平中心，垂直顶部 */
        min-height: 100px;
    }
    ```

- `background-attachment`

    `background-attachment` 决定了背景图像是随内容滚动还是在页面滚动时保持固定。

    主要取值:
    - `scroll` （默认值），背景图像随内容滚动
    - `fixed` ，背景图像保持在屏幕上的同一位置。

    ```css
    body {
        background-image: url('https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg');
        background-position: center top;
        background-attachment: fixed; /** 背景图像保持在固定位置 */
    }
    ```

---

`background` 属性可以将上述几个属性合并到一起进行设置:

```css
body {
    background: center top fixed
        url('https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg');
}
```

上述代码相当于将 `background-image` 设置为 `url('https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg');`，将 `background-position` 设置为 `center top`， 将 `background-attachment` 设置为 `fixed`

### 背景渐变

CSS 中有两种主要类型的渐变：**线性渐变** 和 **径向渐变**

#### 线性渐变 linear-gradient

线性渐变是指颜色沿直线过渡。您可以定义渐变的方向和涉及的颜色。

基本语法:

```css
selector {
    background: linear-gradient(direction, color-stop1, color-stop2, ...);
}
```

- `direction` 是指渐变方向，可以是关键词如 `to right`, `to bottom`; 也可以是具体的角度如 `45deg` （45° 方向）

- `color-stop` 颜色停止点

下面看一个具体的例子:

```css
.linear-gradient {
    background: linear-gradient(to right, red, yellow);
    height: 40vh;
}
```

如果只想中间的某一部分施行颜色渐变，可以指定颜色占比：

```css
.linear-gradient {
    /* 0%-30% 纯红，30%-70% 红黄渐变，70%-100% 纯黄 */
    background: linear-gradient(to right, red 30%, yellow 70%);
    height: 40vh;
}
```

#### 径向渐变 radial-gradient

径向渐变是指颜色从 **原点**（通常是中心）向外呈圆形或椭圆形辐射过渡。

基本语法:

```css
selector {
    background: radial-gradient(
        shape size at position,
        color-stop1,
        color-stop2,
        ...
    );
}
```

- `shape` 指定渐变形状， 如 `circle`, `ellipse`

- `size` 决定了渐变结束形状的大小, 主要取值： `closest-side` 、 `closest-corner` 、 `farthest-side` 或 `farthest-corner`

- `position` 决定渐变中心的位置，可以使用关键字如 `center`, `top left`, `bottom right`；也可以使用精确值如 `50% 50%`, `10px 20px` 等

- `color-stop` 是颜色停止点

具体示例:

```css
.radial-gradient {
    background: radial-gradient(
        circle closest-side at center,
        red,
        yellow 50%,
        green
    );
    height: 60vh;
}
```

### 给图片添加边框

#### border 属性

给图片添加边框最直接的方法是使用 `border` 属性。这个属性是一种简写方式，可以让你一次性设置边框的宽度、样式和颜色。

```css
img {
    border: 2px solid red;
}
```

如果需要对边框的各个边进行更精细的控制，可以使用每个边的特定边框属性：

```css
img {
    border-top: 10px solid red;
    border-right: 10px dashed green;
    border-bottom: 10px dotted blue;
    border-left: 10px double purple;
}
```

#### outline 属性

创建边框效果的另一种方法是使用 `outline` 属性。 `outline` 不会影响元素的尺寸或布局：

```css
img {
    outline: 3px solid gold;
}
```

#### 给边框设置圆角

如果要为边框创建圆角，可以将 `border-radius` 属性与 `border` 属性结合使用：

```css
img {
    border: 2px solid black;
    border-radius: 10px;
}
```

## 设计 Design

### 常见设计相关术语

#### 布局 Layout

布局是指在页面或屏幕上如何排列视觉元素以传达信息。这些元素可能包括文本、图像和留白。布局就像设计的蓝图。设计师必须考虑每个元素的位置、大小和层级关系。

#### 对齐 Alignment

对齐是指元素彼此之间的放置关系。

#### 构图 Composition

构图是安排元素以创造和谐设计的艺术。

布局主要关注元素的放置位置，而构图还会考虑这种放置方式对整体设计的艺术影响。

#### 平衡 Balance

平衡是指 **视觉重量** 在画面中的分布方式。设计师力求通过对称或不对称的布局来创造一种平衡感。平衡的设计给人以和谐之感。

#### 层级 Hierarchy

层级确立了设计中各个元素的优先顺序，确保最重要的信息首先被注意到。你可以通过大小、颜色、对比度、对齐方式、留白甚至字体来实现视觉层级。

#### 对比度 Contrast

使用合适的对比度可以清晰的展现各个元素，高对比度能提高可读性。

#### 留白 White Space

留白，也称为“负空间”，是指设计中的空白区域，也就是元素周围的区域。你可能会惊讶地发现，留白不一定是白色的。实际上，它可以是任何颜色或纹理的空间。留白的作用是提高设计的可读性，并增强视觉层次感。

#### 用户界面 User Interface, UI

用户界面（也称 UI）是指人与计算机交互的方式。用户界面包括用户在屏幕上可以看到的视觉和交互元素，例如图标、图像、文本、菜单、链接和按钮。

#### 用户体验 User Experience, UX

用户体验（UX）是指用户在使用产品或服务时的感受。一款用户体验设计良好的应用程序应该直观易用、高效便捷、方便访问且令人愉悦。用户界面在提升用户体验的便捷性和愉悦感方面起着关键作用，因此两者密切相关。

### 如何设计良好的背景和前景对比？

**对比度** 是指两种颜色之间的差异，或者说，区分它们的难易程度。

对比度越高的颜色在视觉上就越容易区分，而对比度越低的颜色在视觉上就越相似。

但如何判断对比度是否“足够好”呢？你不能仅仅根据文本的视觉效果来判断，因为每个用户的体验都不同。

WCAG（网页内容无障碍指南，Web Content Accessibility Guidelines）给我们提供了标准：

- 对比度为 `4.5:1` 的文本被认为是 AA 标准，这是确保大多数用户都能访问的最低标准。

- 对比度为 `7:1` 的文本被认为是 AAA 标准，可确保最佳的可访问性。

有很多网站可以检查两种颜色之间的对比度，但大多数浏览器都允许您直接在网站的开发者工具中执行此操作。

<img src="imgs/01.png" alt="使用 chrome 开发者工具的 css overview 查看对比度" style="max-width:800px"><br>
<img src="imgs/02.png" alt="使用 chrome 开发者工具的 color picker 查看对比度" style="max-width:800px"><br>

下面是一个演示对比度的示例：

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>freeCodeCamp</title>
        <link rel="stylesheet" href="styles.css" />
    </head>
    <body>
        <div class="contrast-21">
            <span class="label">Contrast Ratio 21:1</span>
            This is black text on a white background, which has the highest
            contrast ratio of 21:1.
        </div>

        <div class="purple-on-blue">
            <span class="label">Purple on Blue (Lower Contrast)</span>
            This doesn't meet the AA standard.
        </div>

        <div class="red-on-blue">
            <span class="label">Red on Blue (Higher Contrast Hue Shift)</span>
            This doesn't meet accessibility standards.
        </div>

        <div class="low-sat-red-on-blue">
            <span class="label"
                >Low Saturation Red on Blue (Contrast ~1.49:1)</span
            >
            This red has low saturation, resulting in a poor contrast ratio.
        </div>

        <div class="high-sat-red-on-blue">
            <span class="label"
                >Higher Saturation Red on Blue (Contrast ~3.54:1)</span
            >
            Increasing the saturation of red improves contrast but it’s still
            below AA standard.
        </div>

        <div class="dark-red-on-light-blue">
            <span class="label"
                >Darker Red on Light Blue (Contrast ~10.34:1)</span
            >
            Decreasing the lightness of the red increases the contrast ratio
            significantly.
        </div>
    </body>
</html>
```

```css
.contrast-21 {
    background-color: white;
    color: black;
    padding: 15px;
    font-family: sans-serif;
    font-size: 18px;
    margin-bottom: 20px;
}

.label {
    font-weight: bold;
    margin-bottom: 8px;
    display: block;
}

.purple-on-blue {
    background-color: #0000cc;
    color: #800080;
    padding: 15px;
    font-family: sans-serif;
    font-size: 18px;
    margin-bottom: 20px;
}

.red-on-blue {
    background-color: #0000cc;
    color: #ff0000;
    padding: 15px;
    font-family: sans-serif;
    font-size: 18px;
    margin-bottom: 20px;
}

.low-sat-red-on-blue {
    background-color: #0000cc;
    color: #b23333;
    padding: 15px;
    font-family: sans-serif;
    font-size: 18px;
    margin-bottom: 20px;
}

.high-sat-red-on-blue {
    background-color: #0000cc;
    color: #ff4d4d;
    padding: 15px;
    font-family: sans-serif;
    font-size: 18px;
    margin-bottom: 20px;
}

.dark-red-on-light-blue {
    background-color: #add8e6;
    color: #8b0000;
    padding: 15px;
}
```

### 以用户为中心的设计

#### 什么是以用户为中心的设计？

以用户为中心的设计是一种网页开发方法，它优先考虑最终用户，包括他们的需求、偏好和限制。

以用户为中心的设计首先要考虑的是目标用户群体。例如，如果你的目标用户群体比较年轻，你可以采用更炫酷、更吸引眼球的设计，迅速抓住他们的注意力。而对于年龄较大的用户群体，你则应该更注重简洁明了、避免干扰的设计。

用户行为也是一个重要因素。您需要利用分析工具（例如 Google Analytics）来衡量用户如何与您的页面互动。这可以揭示用户可能遇到的“卡住”并离开页面的地方，或者发现改进整体交互流程的机会。

以用户为中心的设计关键在于真正让用户参与其中。提供一个反馈渠道，让用户分享他们在使用网站的体验和痛点，可以帮助你收集重要信息并进行迭代改进。归根结底，以用户为中心的设计意味着你需要将用户置于决策的首位，无论是通过调研还是直接反馈。

#### 用户研究、用户测试和用户需求

**用户研究** 是对使用您产品的人群进行系统性研究。其目标是衡量用户的需求、行为和痛点。

用户研究的形式多种多样。其中最常见的或许是 **净推荐值（Net Promoter Score，NPS）**。NPS 衡量的是用户向朋友推荐您产品的可能性。

NPS 的测量方法是在用户使用过程中的关键节点（例如 7 天、30 天和 90 天后）进行调查。NPS 的评分范围为 0 到 10，9 分和 10 分表示用户是您网站的积极推荐者。

另一种研究方法是用户流失调研。这是一种在用户取消订阅或删除帐户时向他们展示的调查问卷。通过这项调查，您可以深入了解导致用户流失的因素，从而采取相应的措施。

**用户测试** 指的是在用户与应用程序交互时收集数据的过程。

作为一名 Web 开发人员，你可能会遇到 A/B 测试。A/B 测试是指将新功能推送给随机选择的用户群体子集。然后，你可以利用分析数据来确定该功能是否有效。

**用户需求** 指的是应用程序需要遵循的故事或准则。它可以指导开发过程。用户需求可以通过用户调研、行业标准或利益相关者的反馈来定义。

#### 深色模式

深色模式是网页应用程序的一项特殊功能，它可以将默认的浅色配色方案更改为深色配色方案。这有助于减少眼睛疲劳，并提高弱光环境下的阅读体验。在设计深色模式功能时，了解最佳实践至关重要，以确保其有效且易于使用。

最佳实践：

- 在深色模式下应避免使用饱和度高的颜色。在深色模式下，低饱和度的颜色视觉效果更舒适

- 相比于纯黑背景搭配白色文字，建议使用深灰色背景搭配浅灰色文字，以获得更柔和的对比度。

- 在实施深色模式时，您应该考虑如何使深色模式功能与品牌的颜色和风格保持一致。
    - 品牌标识是一组代表品牌的视觉元素，例如徽标、颜色和字体。
    - 将品牌图标和按钮设置为全饱和度，而周围元素降低饱和度，也是可以的。

在设计时，始终要关注用户体验和对比度。深色模式也不例外，遵循以下最佳实践，即可创建高效且用户友好的深色模式功能。

#### 面包屑导航

在网页层级比较深的网站上经常可以看到类似 `Homepage/articles/java/jvm` 这样子的导航，这种导航称为 **面包屑导航（Breadcrumb Navigation）**

最佳实践：

- 只有在网页层级复杂的设计中才应该使用这种导航

- 面包屑导航应该放在显眼的位置，方便用户找到。一般放在主导航栏的上方或者下方

- 面包屑导航的字体不能太小，但也不能太大（防止长路径占用过多空间）

#### 卡片设计

最佳实践：

- 卡片设计的首要原则是 **简洁**。

- 需要考虑用户可以点击卡片的位置。
    - 有些卡片设计只有一个按钮，用户可以很直观地知道点击位置。
    - 而另一些卡片设计则允许整个卡片都可点击。当用户将鼠标悬停在卡片的任何部分时，卡片会改变颜色或添加阴影效果，以提示该卡片可点击。
    - 无论选择哪种设计，都必须在整个网站中保持一致，并且易于用户理解。

- 卡片上媒体素材的使用
    - 选择高质量的媒体素材可以显著提升用户体验。

- 色彩层级的使用
    - 你需要确保卡片上最重要的信息最为醒目。你可以使用鲜艳的颜色来表示重要元素，例如行动号召按钮（call-to-action，CTA），而使用浅色来表示卡片上不太重要的元素。

#### 无限滚动

无限滚动是一种设计模式，它会随着用户向下滚动页面而加载更多内容。这种模式常用于 Twitter 等社交媒体网站。

无限滚动也常被用来替代分页。分页是一种将内容分成多个页面的设计模式。当需要显示大量内容时，通常会使用分页。

最佳实践：

- 要提供一个“加载更多”按钮，用户点击后即可加载下一组结果。这样可以让用户更好地控制何时查看更多内容。

- 另一个可以考虑的方案是添加“返回”按钮。这样用户无需向上滚动即可返回上一页。这能提升用户体验，并让他们更好地掌控浏览过程。

- 有时你会看到一些设计中带有“返回顶部”按钮，点击即可返回搜索结果页面的顶部。另一个需要考虑的因素是提供加载指示器。用户应该能够清晰地看到正在加载更多内容；否则，他们可能会误以为页面出现故障。

- 确保用户能够随时访问页脚。如果页脚包含重要信息，则应确保用户始终可以访问。

#### 模态对话框 Modal Dialog

模态对话框（Modal Dialog Box）是一种弹窗界面元素，它会强制打断用户的操作流程。在关闭该对话框或做出响应（如点击“确定”或“取消”）之前，用户无法与主窗口或应用程序的其他部分进行交互。

HTML 中有一个 `dialog` 元素，可以用来创建模态框。

```html
<button id="open-modal">Open Modal</button>
<dialog>
    <h2>Subscribe to our Newsletter!</h2>
    <p>Get the latest updates and offers.</p>
    <button>Subscribe</button>
    <button>Close</button>
</dialog>
```

```css
dialog {
    border: none;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

dialog::backdrop {
    background: rgba(0, 0, 0, 0.5);
}
```

```js
const dialog = document.querySelector('dialog');
const closeButton = dialog.querySelector('button:last-of-type');
const openModalButton = document.getElementById('open-modal');

closeButton.addEventListener('click', () => {
    dialog.close();
});

openModalButton.addEventListener('click', () => {
    dialog.showModal();
});

// Close the modal when clicking outside of it
dialog.addEventListener('click', (event) => {
    const rect = dialog.getBoundingClientRect();
    const isInDialog =
        event.clientX >= rect.left &&
        event.clientX <= rect.right &&
        event.clientY >= rect.top &&
        event.clientY <= rect.bottom;
    if (!isInDialog) {
        dialog.close();
    }
});
```

- 允许用户点击模态框外部将其关闭始终是一个好主意。

- 模态框也应该有关闭按钮。虽然你可能很希望用户点击你的行动号召按钮，但重要的是要让他们可以选择退出模态框，并继续他们之前正在进行的操作。

#### 进度指示 Progress Indication

进度指示是一种向用户展示他们在流程中所处阶段的方式。它可以用于表单、注册和设置流程中。其目的是帮助用户了解他们所处的流程阶段以及还需要完成多少步骤。

最佳实践：

- 保持简洁

- 允许用户返回到之前的步骤

- 确保进度指示部分易于查找

- 要有清晰的章节标题、百分比或步骤说明

一个示例：

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>freeCodeCamp</title>
        <link rel="stylesheet" href="styles.css" />
    </head>
    <body>
        <form id="multiStepForm">
            <div class="form-progress">
                <label class="progress-label">Form progress</label>
                <div class="progress-container">
                    <div class="progress-bar"></div>
                    <div class="progress-text">Step 1 of 3</div>
                </div>
            </div>

            <!-- Step 1 -->
            <fieldset class="form-step active">
                <legend>Personal Information</legend>
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required />

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required />

                <button type="button" class="next-btn">Next</button>
            </fieldset>

            <!-- Step 2 -->
            <fieldset class="form-step">
                <legend>Address</legend>
                <label for="address">Street Address:</label>
                <input type="text" id="address" name="address" required />

                <label for="city">City:</label>
                <input type="text" id="city" name="city" required />

                <button type="button" class="prev-btn">Previous</button>
                <button type="button" class="next-btn">Next</button>
            </fieldset>

            <!-- Step 3 -->
            <fieldset class="form-step">
                <legend>Review & Submit</legend>
                <p>Please review your information before submitting.</p>

                <button type="button" class="prev-btn">Previous</button>
                <button type="submit">Submit</button>
            </fieldset>
        </form>

        <script src="index.js"></script>
    </body>
</html>
```

```css
.form-progress {
    max-width: 500px;
    margin: 20px auto 30px;
    font-family: Arial, sans-serif;
}

.progress-label {
    display: block;
    margin-bottom: 8px;
    font-size: 16px;
    font-weight: 600;
    color: #333;
}

.progress-container {
    position: relative;
    background-color: #555;
    border-radius: 8px;
    height: 30px;
    overflow: hidden;
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.3);
}

.progress-bar {
    background-color: #4caf50;
    height: 100%;
    width: 0;
    border-radius: 8px 0 0 8px;
    transition: width 0.3s ease;
}

.progress-text {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 30px;
    line-height: 30px;
    text-align: center;
    font-weight: bold;
    color: #fff;
    pointer-events: none;
    user-select: none;
}

form {
    max-width: 500px;
    margin: 0 auto;
    font-family: Arial, sans-serif;
}

fieldset {
    border: none;
    padding: 0;
    margin: 0 0 20px;
}

legend {
    font-size: 1.2em;
    font-weight: 700;
    margin-bottom: 10px;
    color: #222;
}

label {
    display: block;
    margin-bottom: 6px;
    font-weight: 600;
    color: #333;
}

input[type='text'],
input[type='email'] {
    width: 100%;
    padding: 8px 10px;
    font-size: 1em;
    border: 1px solid #ccc;
    border-radius: 4px;
    margin-bottom: 15px;
    box-sizing: border-box;
    transition: border-color 0.2s ease;
}

input[type='text']:focus,
input[type='email']:focus {
    outline: none;
    border-color: #4caf50;
    box-shadow: 0 0 5px rgba(76, 175, 80, 0.5);
}

.form-step {
    display: none;
}

.form-step.active {
    display: block;
}

button {
    background-color: #4caf50;
    border: none;
    color: white;
    padding: 10px 18px;
    font-size: 1em;
    border-radius: 5px;
    cursor: pointer;
    margin-right: 10px;
    transition: background-color 0.2s ease;
}

button:hover:not(:disabled) {
    background-color: #45a049;
}

button:disabled {
    background-color: #9e9e9e;
    cursor: not-allowed;
}

@media (max-width: 600px) {
    .form-progress,
    form {
        max-width: 90%;
        margin: 20px auto;
    }
}
```

```js
const form = document.getElementById('multiStepForm');
const steps = form.querySelectorAll('.form-step');
const progressBar = form.querySelector('.progress-bar');
const progressText = form.querySelector('.progress-text');
const totalSteps = steps.length;

let currentStep = 0;

function updateProgress() {
    const percent = ((currentStep + 1) / totalSteps) * 100;
    progressBar.style.width = percent + '%';
    progressText.textContent = `Step ${currentStep + 1} of ${totalSteps}`;
}

function showStep(index) {
    steps.forEach((step, i) => {
        step.classList.toggle('active', i === index);
    });
    updateProgress();
}

form.querySelectorAll('.next-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
        if (currentStep < totalSteps - 1) {
            currentStep++;
            showStep(currentStep);
        }
    });
});

form.querySelectorAll('.prev-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
        if (currentStep > 0) {
            currentStep--;
            showStep(currentStep);
        }
    });
});

showStep(currentStep);

form.addEventListener('submit', (e) => {
    e.preventDefault();
    alert('Form submitted!');
});
```

#### 购物车

最佳实践：

- 确保用户始终可以看到购物车。大多数购物车设计都会将其显示在页面右上角。

- 用户应该能够在购物车图标旁边看到购物车中的商品数量，并且可以点击购物车查看所购商品的更多详细信息。

- 为用户提供清晰便捷的方式来更新购物车中的商品数量。这可以通过在购物车中每个商品旁边添加数量输入框来实现。用户只需在输入框中更改数字即可轻松更新商品数量。

- 您还应该在购物车中的每个商品旁边提供一个“移除”按钮。这样用户就可以轻松地从购物车中移除商品。

- 购物车图标应该易于所有用户识别。常见的图标是带把手和轮子的购物车。其他图标可以是购物袋或购物篮。但你不希望选择过于抽象或难以理解的图标。

- 当用户想要查看购物车总价时，应该能够轻松找到购物车中所有商品的总价。总价应该醒目地显示在页面上，以免用户费力查找。

- 您应该提供一个清晰的行动号召按钮（CTA），引导用户进入结账页面。

### 通用设计工具

#### 设计简报 Design Briefs

在设计新功能或应用程序时，一个好的第一步是制定设计简报。

设计简报是一份文件，它概述了项目的目标和需求。它就像一张路线图，指导设计过程，并确保最终产品满足客户的需求。

设计简报中应包含几个关键要素：

- 对项目和业务的概述。该概述应包括公司的详细信息、使命、价值观、独特卖点以及产品或服务。

- 记录项目的目标和目的
    - 预期成果
    - 增加网站流量或将每月页面访问量增加 X%

- 设计简报应包含目标受众的人口统计信息、兴趣爱好和需求

- 应包括交付成果、时间表和预算。 交付成果应包括项目过程中将要产出的所有物品清单，例如模型和最终设计。

项目设计面临的挑战之一是时间安排和预算控制。在既定的时间和预算范围内，对能够实现的目标保持务实的态度至关重要。因此，制定一份概述这些限制条件的设计简报非常重要。

#### 开发人员应该了解的一些常用设计工具

- **Figma**

    Figma 是开发者应该掌握的最常用、最基本的界面设计工具之一。

    这款基于云端的工具专注于用户界面和用户体验 (UI/UX) 设计。它支持设计和开发团队随时随地协作，并提供以下内置功能：
    - Vector-based design 基于矢量的设计
    - Automatic layout 自动布局
    - Commenting and feedback system 评论和反馈系统
    - Version history 版本历史记录
    - Real-time collaboration 实时协作
    - Design systems, and more. 设计系统等等。

    要开始使用 Figma，您可以使用其网页版界面，也可以下载桌面应用程序到您的电脑上。它提供丰富的免费功能，因此您无需购买专业版即可完成许多工作。

- **Sketch**

    Sketch 是开发者应该熟悉的另一款重要设计工具。与 Figma 类似，它基于矢量图形，主要用于 UI/UX 设计。

    Sketch 因其直观的界面和简洁性而广受欢迎，是开发人员快速创建原型的不二之选。它也被设计师广泛用于创建用户界面、图标和网页布局等任务。

    Sketch 的主要局限在于它缺乏基于云的界面，并且只能在 macOS 上使用。

- **Adobe XD**

    Adobe XD 是另一款基于矢量的 UI/UX 设计原型制作工具，以其与 Photoshop、Illustrator 和 After Effects 等其他 Adob​​e 应用程序的无缝集成而闻名。

    Adobe XD 同时支持 Windows 和 macOS 系统，并包含基于云端的界面。

- **Canva**

    你可以使用 Canva 创建各种视觉内容，包括海报、封面照片、演示文稿、短视频等等。它用户友好且简洁的设计使其成为初学者的理想之选。

    此外，Canva 还提供丰富的模板、图像和设计元素库，使创建专业外观的设计变得轻松便捷。

    Canva 还支持网页界面设计，并允许与团队成员协作。该平台可在网页、桌面端、安卓和 iOS 应用上使用。

- **其他工具**

    其他开发人员应该了解的常用设计工具包括 Framer、InVision、Adobe Photoshop、Adobe Illustrator 和 Miro。

## 单位

在设计页面时，您会用到各种属性，例如宽度、高度、内边距、外边距等等。定义这些属性时，您需要指定要使用的长度单位。

可以使用两种单位：**相对单位** 和 **绝对单位**。

### 绝对单位 Absolute Unit

最常用的绝对单位是 **像素**（`px`），像素是 CSS 中的固定尺寸计量单位，可以精确控制尺寸。这意味着 `1` 像素始终等于 `1/96` 英寸。

需要注意的是，虽然 1px 在 CSS 布局中被标准化为 1/96 英寸，但像素的实际物理尺寸可能会因显示器而异。

其他类型的绝对单位：

- `in`, 表示 inch，等于 96 个像素

- `cm`， 厘米 `1 cm = 25.2/64 inch`

- `mm`，毫米

- `q`，四分之一毫米 `1 q = 1/40 cm`

- `pc`，Pica 派卡 `1 pc = 1/6 inch`

- `pt`，Point 点 `1 pt = 1/72 inch`

这些单位大部分都用于打印而非屏幕显示

### 百分比

CSS 中的百分比是 **相对单位**，允许您将大小、尺寸和其他属性定义为其 **父元素的比例**。使用百分比值时，您实际上是在说：“将此元素的大小设置为其容器的 X%”。

百分比非常适合创建能够适应各种屏幕尺寸的自适应布局。例如，将容器的 width: 80% 即可确保无论在何种设备上，它都占据其父元素宽度的 80%。

### em & rem

#### em

`em` 单位是相对于元素的字体大小而言的。如果字体大小属性本身使用了 `em` 单位，那么它将会是相对于父元素的字体大小而言的。

举个例子：

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>freeCodeCamp</title>
        <link rel="stylesheet" href="styles.css" />
    </head>
    <body>
        <p class="para">I am a paragraph element</p>

        <div class="blue-box"></div>
    </body>
</html>
```

```css
.para {
    font-size: 20px;
    margin-bottom: 1.5em; /** 因为当前元素设置了 font-size 属性，所以这里的 1.5em = 30px */
    border: 2px solid red;
}

.blue-box {
    background-color: blue;
    color: white;
    padding: 10px;
    width: 100px;
    height: 100px;
}
```

一个段落，一个方块。我们给段落的底部设置了 `1.5em` 的距离，前面说了 `em` 单位是相对于元素的字体大小而言的，段落的字体大小是 `20px`，因此这里的 `1.5em` 其实等于 `30px`

若是我们将 `.para` 的 `font-size` 属性给去掉，那么 `margin-bottom` 的 `1.5em` 则是相对于父元素的字体大小而言，其父元素是 `body`，`body` 没有默认的 `font-size`, 但它会继承 `html`的 `font-size`，`html` 的默认字体大小是 `16px`，因此，这里的 `1.5em` 将会是 `24px`

> CSS 中，`font-size` 是一个 **继承属性**。如果当前元素没有显式设置 `font-size`，它不会直接去“看”父元素有没有写 `font-size` 样式，而是 **直接继承父元素计算后的最终字体大小**。

其实本质上是这样处理的：

- 如果父元素也没有设置，就继承祖父元素的。

- 如果所有祖先都没有设置，最终会一直追溯到根元素 `<html>`。

- 如果 `<html>` 也没有设置，浏览器会使用默认值，通常是 `16px`。

#### rem

rem 单位是相对于根元素，即 `<html>` 元素的字体大小而言的

默认情况下，浏览器赋予 `<html>` 的默认字体大小是 `16px`, 如果用户在浏览器设置中增大字体，那么 `<html>` 元素的字体会增大，从而所有 `rem` 单位都会按比例进行缩放

```css
.para {
    font-size: 1.2rem; /** rem 是相对于 html 元素的 font-size 而言的, 假设 html 的 font-size 是 16px, 那么 1.2rem = 19.2px */
    margin-bottom: 1.5em; /** 假设 html 的 font-size 是 16px, 1.5rem = 24px */
    border: 2px solid red;
}
```

与 `em` 的区别:

- `em` 单位是相对于元素自身或其父元素的字体大小的

- `rem` 单位是相对于根元素的字体大小的

### vh & vw

`vh` 和 `vw` 是视口相对单位，允许您根据浏览器窗口的尺寸调整元素大小

`vh` 表示 viewport height （视口高度）， `1vh` 等于视口高度的 `1%`

`vw` 表示 viewport width （视口宽度）， `1vw` 等于视口宽度的 `1%`

### calc()

使用 `calc()` 函数，您可以直接在样式表中执行计算，从而动态确定属性值。

```css
div {
    color: white;
    background-color: #1b1b32;
    width: calc(50% - 20px); /** 50% 表示父容器宽度的 50% */
}
```

如果父容器调整大小, 这个 `width` 属性值会自动进行计算

使用 `calc()` 注意事项：

- 表达式运算符两端最好加上空格，比如 `calc(100% - 30px)`
    - `calc(100% -30px)` 是无效的，因为 `+`, `-` 两端必须要有空格
    - 虽然乘法和除法可以不加空格，但是为了统一，最好在所有运算符两端都加上空格

- 可以嵌套调用 `calc()` 函数

- 如果表达式中有零值，零值也需要带上单位，比如 `calc(100% - 0px)`
    - `calc(100% - 0)` 是无效的

- 使用乘法，其中一个操作数必须是无单位的， `calc(5 * 50px)` 或 `calc(5px * 50)`
    - `calc(5px * 50px)` 是无效的

- 除法中，如果使用两个相同单位的值相除，结果会是一个无单位的值。一般是用一个有单位的值除以一个无单位的量纲

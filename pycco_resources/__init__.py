import pystache

css = """
/*--------------------- Layout and Typography ----------------------------*/
@import url('https://fonts.googleapis.com/css?family=Poiret+One&display=swap');

html, body {
  max-width: 100%;

}

body {
  font-family: 'Andale Mono Regular', 'Currier New', AndaleMono, CurrierNew, serif;
  font-size: 1rem;
  line-height: 1.5rem;
  color: #252519;
  margin: 0;
  padding: 0 ;
  /*background: #f5f5ff;*/
  background: white;
  width: 100%;
  box-sizing: border-box;
  /*overflow-x: hidden;*/
  overflow-x: hidden;
  white-space: nowrap;
}

a {
  color: #261a3b;
}

a:visited {
  color: #261a3b;
}

p {
  margin: 0 0 15px 0;
  /*max-width: 43vw;*/
  max-width: 100%;
  word-break: break-word;
}

h1, h2, h3, h4, h5, h6 {
  margin: 2rem 0 1rem 0rem;
}

h2, h3, h4, h5, h6 {
  margin-top: 0;
}
.docs > h3 {
  text-transform: uppercase;
}
#container {
  background: #f5f5ff;
  width: 42.5%;
  padding-left: 2rem;
}

.section{
  /*border: 1px solid purple;*/
  width: 100%;
  height: fit-content;
  padding-left: 1rem;
}
#container > div:nth-child(2)  {
  background-color: rgba(255, 184, 212, 0.3);

}
.section:hover {
  background-color: rgba(255, 184, 212, 0.3);
  width: 100vw;
}
/*#container, div.section {*/
div.section {
  position: relative;
  /*width: 100%;*/
  width: 100vw;
  margin-bottom: 1rem;

}

/* Clear floats after the columns */
.div.section:after {
  content: "";
  display: table;
  clear: both;
}

#background {
  position: absolute;
  top: 0;
  left: 100%;
  right: 0;
  bottom: 0;
  background: #FFF;
  border-left: 1px solid #e5e5ee;
  z-index: 0;
}

#jump_to, #jump_page {
  background: white;
  -webkit-box-shadow: 0 0 25px #777;
  -moz-box-shadow: 0 0 25px #777;
  -webkit-border-bottom-left-radius: 5px;
  -moz-border-radius-bottomleft: 5px;
  font: 10px Arial;
  text-transform: uppercase;
  cursor: pointer;
  text-align: right;
}

#jump_to, #jump_wrapper {
  position: fixed;
  right: 0;
  top: 0;
  padding: 5px 10px;
}

#jump_wrapper {
  padding: 0;
  display: none;
}

#jump_to:hover #jump_wrapper {
  display: block;
}

#jump_page {
  padding: 5px 0 3px;
  margin: 0 0 25px 25px;
}

#jump_page .source {
  display: block;
  padding: 5px 10px;
  text-decoration: none;
  border-top: 1px solid #eee;
}

#jump_page .source:hover {
  background: #f5f5ff;
}

#jump_page .source:first-child {
}
#text{
  width:50%;
}

/* code part */
div.docs {
  float: left;
  /*max-width: 45vw;*/
  width: 40%;

  /*min-width: 500px;*/
  min-height: 5px;

  /*padding: 10px 25px 1px 50px;*/
  padding: 0 0 0 0;
  vertical-align: top;
  text-align: left;
  white-space: initial;

}

.docs pre {
  margin: 1rem 0 1rem;
  padding-left: 1rem;
}

.docs p tt {
  background: #f8f8ff;
  border: 1px solid #dedede;
  font-size: 1rem;
  padding: 0 0.2em;
}
.docs p code {
  background: white;
  border: 1px solid #dedede;
  font-size: 1rem;
  padding: 0 0.2em;
}
.octowrap {
  position: relative;
}

.octothorpe {
  /*font: 12px Arial;*/
  text-decoration: none;
  color: #454545;
  position: absolute;
  /*top: 3px;*/
  left: -1rem;
  padding: 1px 2px;
  opacity: 0;
  -webkit-transition: opacity 0.2s linear;
}

div.docs:hover .octothorpe {
  opacity: 1;
}

div.docs > pre > code {
  width: 45vw;
  font-size: .8rem;
  margin-left: 1rem;
}
/*div.docs > pre > code #text{*/
/*  width: 30vw;*/
/*  border: 1px solid purple;*/
/*  font-size: .8rem;*/
/*}*/

div.code {
  /*margin-left: 45vw;*/
  /*padding: 14px 15px 16px 50px;*/
  padding: 1rem 0 0 0;
  vertical-align: top;

}
code{
  word-break: break-word;
  white-space:pre-line;
  max-width:40vw;
}
.code pre, .docs p code {
  font-size: .8rem;
  line-height: 1.15rem;
  /*white-space: initial;*/
  /*word-break: break-word;*/
  width: auto;
}
/*.code pre {*/
/*  border: 1px solid red;*/
/*}*/
.docs p code {
  border: 1px solid blue;
}
pre, tt, code {
  line-height: 1.15rem;
  font-family: AndaleMono, 'Andale Mono Regular', monospace;
  margin: 0;
  padding: 0;
}
.docs p code:not(.highlight) {
  display:inline-block;
}
div.docs > ol > li , div.docs > ul > li{
  max-width: 90%;
}
pre > code:not(.highlight) {
  width: inherit;
  word-break: break-word;
  z-index: 1;
  display: block;
  /*border: 1px solid green;*/
  margin: 0;
  /*padding 0;*/
  position: relative;
  left: -1.5rem;
  padding-left: 1rem;
  /*text-indent: -2em;*/
}
/*pre > code:not(.highlight)::first-line {*/
/*    padding-left: 0em;*/
/*}*/
/*.docs > p::before{*/
/*  content: "# ";*/
/*}*/


.docs > p {
  /*border: 1px solid pink;*/
  width: 95%;
  margin:0;
  /*margin: 0 0 0 .5rem;*/
  /*font-family: 'Indie Flower', cursive;*/
  /*font-family: 'Gochi Hand', cursive;*/
  /*font-family: 'Handlee', cursive;*/
  font-family: 'Poiret One', cursive;
  /*font-family: 'Fredericka the Great', cursive;*/
  /*font-family: 'Caveat Brush', cursive;*/

  font-size: 1.25rem;




}

div.clearall {
  clear: both;
}


.highlight, .highlight > pre {
  z-index: 2;
  word-break: break-word;
  width: fit-content;
  margin-left: .5rem;
}
.highlight > pre > span {
  white-space: initial;
}


div.docs > ol > li, div.docs > ul > li {
  font-size: .75rem;
}

.docs p::first-letter {
  text-transform: capitalize;
}

/*span h3 {*/
/*    text-transform: uppercase;*/
/*}*/
div.section{
  display: flex;
}
.section .docs {
  width: 40%;
  /*margin-right: -1rem;*/

}

.section .code {
  width: 50%;
}
/*---------------------- Syntax Highlighting -----------------------------*/
td.linenos {
  background-color: #f0f0f0;
  padding-right: 10px;
}

span.lineno {
  background-color: #f0f0f0;
  padding: 0 5px 0 5px;
}

body .hll {
  background-color: #ffffcc
}

body .c {
  color: #408080;
  font-style: italic
}

/* Comment */
body .err {
  border: 1px solid #FF0000
}

/* Error */
body .k {
  color: #954121
}

/* Keyword */
body .o {
  color: #666666
}

/* Operator */
body .cm {
  color: #408080;
  font-style: italic
}

/* Comment.Multiline */
body .cp {
  color: #BC7A00
}

/* Comment.Preproc */
body .c1 {
  color: #408080;
  font-style: italic
}

/* Comment.Single */
body .cs {
  color: #408080;
  font-style: italic
}

/* Comment.Special */
body .gd {
  color: #A00000
}

/* Generic.Deleted */
body .ge {
  font-style: italic
}

/* Generic.Emph */
body .gr {
  color: #FF0000
}

/* Generic.Error */
body .gh {
  color: #000080;
  font-weight: bold
}

/* Generic.Heading */
body .gi {
  color: #00A000
}

/* Generic.Inserted */
body .go {
  color: #808080
}

/* Generic.Output */
body .gp {
  color: #000080;
  font-weight: bold
}

/* Generic.Prompt */
body .gs {
  font-weight: bold
}

/* Generic.Strong */
body .gu {
  color: #800080;
  font-weight: bold
}

/* Generic.Subheading */
body .gt {
  color: #0040D0
}

/* Generic.Traceback */
body .kc {
  color: #954121
}

/* Keyword.Constant */
body .kd {
  color: #954121;
  font-weight: bold
}

/* Keyword.Declaration */
body .kn {
  color: #954121;
  font-weight: bold
}

/* Keyword.Namespace */
body .kp {
  color: #954121
}

/* Keyword.Pseudo */
body .kr {
  color: #954121;
  font-weight: bold
}

/* Keyword.Reserved */
body .kt {
  color: #B00040
}

/* Keyword.Type */
body .m {
  color: #666666
}

/* Literal.Number */
body .s {
  color: #219161
}

/* Literal.String */
body .na {
  color: #7D9029
}

/* Name.Attribute */
body .nb {
  color: #954121
}

/* Name.Builtin */
body .nc {
  color: #0000FF;
  font-weight: bold
}

/* Name.Class */
body .no {
  color: #880000
}

/* Name.Constant */
body .nd {
  color: #AA22FF
}

/* Name.Decorator */
body .ni {
  color: #999999;
  font-weight: bold
}

/* Name.Entity */
body .ne {
  color: #D2413A;
  font-weight: bold
}

/* Name.Exception */
body .nf {
  color: #0000FF
}

/* Name.Function */
body .nl {
  color: #A0A000
}

/* Name.Label */
body .nn {
  color: #0000FF;
  font-weight: bold
}

/* Name.Namespace */
body .nt {
  color: #954121;
  font-weight: bold
}

/* Name.Tag */
body .nv {
  color: #19469D
}

/* Name.Variable */
body .ow {
  color: #AA22FF;
  font-weight: bold
}

/* Operator.Word */
body .w {
  color: #bbbbbb
}

/* Text.Whitespace */
body .mf {
  color: #666666
}

/* Literal.Number.Float */
body .mh {
  color: #666666
}

/* Literal.Number.Hex */
body .mi {
  color: #666666
}

/* Literal.Number.Integer */
body .mo {
  color: #666666
}

/* Literal.Number.Oct */
body .sb {
  color: #219161
}

/* Literal.String.Backtick */
body .sc {
  color: #219161
}

/* Literal.String.Char */
body .sd {
  color: #219161;
  font-style: italic
}

/* Literal.String.Doc */
body .s2 {
  color: #219161
}

/* Literal.String.Double */
body .se {
  color: #BB6622;
  font-weight: bold
}

/* Literal.String.Escape */
body .sh {
  color: #219161
}

/* Literal.String.Heredoc */
body .si {
  color: #BB6688;
  font-weight: bold
}

/* Literal.String.Interpol */
body .sx {
  color: #954121
}

/* Literal.String.Other */
body .sr {
  color: #BB6688
}

/* Literal.String.Regex */
body .s1 {
  color: #219161
}

/* Literal.String.Single */
body .ss {
  color: #19469D
}

/* Literal.String.Symbol */
body .bp {
  color: #954121
}

/* Name.Builtin.Pseudo */
body .vc {
  color: #19469D
}

/* Name.Variable.Class */
body .vg {
  color: #19469D
}

/* Name.Variable.Global */
body .vi {
  color: #19469D
}

/* Name.Variable.Instance */
body .il {
  color: #666666
}

/* Literal.Number.Integer.Long */


/*STYLE IPYTHON NOTEBOOK*/
/*.text_cell, #notebook-container {*/
/*  background: white;*/
/*}*/
/*.cell {*/
/*  border-top: 1px solid black;*/
/*  padding: 1rem;*/
/*}*/
/*#notebook-container > div.output_wrapper > div.output_subarea.output_stream.output_stdout.output_text {*/
/*  height: 2em;*/
/*  overflow-y: auto;*/
/*  border: 1px solid blue;*/
/*  overflow-x: hidden;*/
/*  scroll: none;*/
/*}*/
/*.highlight.hl-ipython3 {*/
/*  margin: 2rem;*/
/*  background: #f5f5ff;*/
/*  border: 1px solid red;*/
/*  padding: 1rem;*/
/*}*/
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;

}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
#index-section, .content {
  padding: 15px;
  /*background-color: #fff;*/
  min-height: 0;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
#index-docs {
  width: 100%;
}


/*div[id^="section-"] > div.code > div > pre > span:nth-child(103)::before{*/
/*  content: "\A";*/
/*}*/
/*.overflow-visible {*/
/*  white-space: initial;*/
/*}*/

div#notebook {
  background-color: #fff;
  min-height: 0;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
"""
body = """\
<div id='container'>
  <div id="background"></div>
  {{#sources?}}
  <div id="jump_to">
    Jump To &hellip;
    <div id="jump_wrapper">
      <div id="jump_page">
        {{#sources}}
          <a class="source" href="{{ url }}">{{ basename }}</a>
        {{/sources}}
      </div>
    </div>
  </div>
  {{/sources?}}
  <div class='section'>
    <div class='docs'><h1>{{ title }}</h1></div>
  </div>
  <div class='clearall'></div>
  {{#sections}}
  <div class='section' id='section-{{ num }}'>
    <div class='docs'>
      <div class='octowrap'>
        <a class='octothorpe' href='#section-{{ num }}'>#</a>
      </div>
      {{{ docs_html }}}
    </div>
    <div class='code'>
      {{{ code_html }}}
    </div>
  </div>
  <div class='clearall'></div>
  {{/sections}}
</div>
"""
html = """\
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="content-type" content="text/html;charset=utf-8">
  <title>{{ title }}</title>
  <link rel="stylesheet" href="{{ stylesheet }}">
</head>
<body>
<div id='container'>
  <div id="background"></div>
  {{#sources?}}
  <div id="jump_to">
    Jump To &hellip;
    <div id="jump_wrapper">
      <div id="jump_page">
        {{#sources}}
          <a class="source" href="{{ url }}">{{ basename }}</a>
        {{/sources}}
      </div>
    </div>
  </div>
  {{/sources?}}
  <div class='section'>
    <div class='docs'><h1>{{ title }}</h1></div>
  </div>
  <div class='clearall'></div>
  {{#sections}}
  <div class='section' id='section-{{ num }}'>
    <div class='docs'>
      <div class='octowrap'>
        <a class='octothorpe' href='#section-{{ num }}'>#</a>
      </div>
      {{{ docs_html }}}
    </div>
    <div class='code'>
      {{{ code_html }}}
    </div>
  </div>
  <div class='clearall'></div>
  {{/sections}}
</div>
</body>
</html>
"""


def template(source):
    # print("=================================================================")
    # print(source)
    # print("=================================================================")
    return lambda context: pystache.render(source, context)
# Create the template that we will use to generate the Pycco HTML page.
#pycco_template = template(html)
# Only render body
pycco_template = template(body)


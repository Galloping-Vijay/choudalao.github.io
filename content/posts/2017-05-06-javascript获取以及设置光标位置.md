---
title: "javascript获取以及设置光标位置"
date: 2017-05-06T12:53:30+08:00
updated: 2026-02-23T07:34:53+08:00
author: "臭大佬"
categories: [前端]
description: "javascript获取以及设置光标位置"
cover: "http://www.choudalao.com/uploads/20191016/8541k3UGBo91mOulvOnfIj689MRTSVqrYgrVgCXy.jpeg"
click: 2902
---

<p><br></p><h2 id="h2_0" pingfang="" lantinghei="" open="" hiragino="" sans="" microsoft="" wenquanyi="" micro="" white-space:="" background-color:="">一. 获取光标位置：</h2><p><br></p><pre lay-lang="JavaScript"><code class="JavaScript">function getCursortPosition (textDom) {    
var cursorPos = 0;    
if (document.selection) {        
    // IE Support
   textDom.focus ();        
   var selectRange = document.selection.createRange();
   selectRange.moveStart ('character', -textDom.value.length);
   cursorPos = selectRange.text.length;
}else if (textDom.selectionStart || textDom.selectionStart == '0') {        
        // Firefox support
    cursorPos = textDom.selectionStart;
}    
return cursorPos;
}</code></pre><p><br></p><h2 id="h2_1" pingfang="" lantinghei="" open="" hiragino="" sans="" microsoft="" wenquanyi="" micro="" white-space:="" background-color:="">二. 设置光标位置：</h2><p><br></p><pre lay-lang="JavaScript"><code class="JavaScript">// 设置光标位置
function setCaretPosition(textDom, pos){    
if(textDom.setSelectionRange) {        
    // IE Support
  textDom.focus();
  textDom.setSelectionRange(pos, pos);
}else if (textDom.createTextRange) {        
    // Firefox support
   var range = textDom.createTextRange();        
   range.collapse(true);        
   range.moveEnd('character', pos);        
   range.moveStart('character', pos);        
   range.select();
    }
}</code></pre><h2 id="h2_2" pingfang="" lantinghei="" open="" hiragino="" sans="" microsoft="" wenquanyi="" micro="" white-space:="" background-color:=""><br></h2><h2 id="h2_2" pingfang="" lantinghei="" open="" hiragino="" sans="" microsoft="" wenquanyi="" micro="" white-space:="" background-color:="">三. 获取选中文字：</h2><p><br></p><pre lay-lang="JavaScript"><code class="JavaScript">// 获取选中文字
function getSelectText() {    
var userSelection, text;    
if (window.getSelection) {        
// Firefox support
  userSelection = window.getSelection();
} else if (document.selection) {        
// IE Support
  userSelection = document.selection.createRange();
}
if (!(text = userSelection.text)) {
  text = userSelection;
 }    
return text;
}</code></pre><h2 id="h2_3" pingfang="" lantinghei="" open="" hiragino="" sans="" microsoft="" wenquanyi="" micro="" white-space:="" background-color:=""><br></h2><h2 id="h2_3" pingfang="" lantinghei="" open="" hiragino="" sans="" microsoft="" wenquanyi="" micro="" white-space:="" background-color:="">四. 选中特定范围的文本：</h2><p><br></p><pre lay-lang="JavaScript"><code class="JavaScript">/**
* 选中特定范围的文本
* 参数：
*     textDom  [JavaScript DOM String] 当前对象
*     startPos  [Int]  起始位置
*     endPos  [Int]  终点位置
*/
function setSelectText(textDom, startPos, endPos) {    
var startPos = parseInt(startPos),endPos = parseInt(endPos),textLength = textDom.value.length;    
if(textLength){        
    if(!startPos){
       startPos = 0;
  }        
  if(!endPos){
      endPos = textLength;
  }        
  if(startPos &gt; textLength){
      startPos = textLength;
  }        
  if(endPos &gt; textLength){
       endPos = textLength;
  }        
  if(startPos &lt; 0){
       startPos = textLength + startPos;
  }        
  if(endPos &lt; 0){
        endPos = textLength + endPos;
  }        
  if(textDom.createTextRange){            
            // IE Support
       var range = textDom.createTextRange();            
       range.moveStart("character",-textLength);            
       range.moveEnd("character",-textLength);            
       range.moveStart("character", startPos);            
       range.moveEnd("character",endPos);            
       range.select();
  }else{            
           // Firefox support
      textDom.setSelectionRange(startPos, endPos);
      textDom.focus();
  }
}
}</code></pre><p><br></p><h2 id="h2_4" pingfang="" lantinghei="" open="" hiragino="" sans="" microsoft="" wenquanyi="" micro="" white-space:="" background-color:="">五. 在光标后插入文本：</h2><p><br></p><pre lay-lang="JavaScript"><code class="JavaScript">/**
* 在光标后插入文本
* 参数：
*     textDom  [JavaScript DOM String] 当前对象
*     value  [String]  要插入的文本
*/
function insertAfterText(textDom, value) {    
    var selectRange;    
    if (document.selection) {        
        // IE Support
    textDom.focus();
    selectRange = document.selection.createRange();
    selectRange.text = value;
    textDom.focus();
  }else if (textDom.selectionStart || textDom.selectionStart == '0') {        
      // Firefox support
    var startPos = textDom.selectionStart;        
    var endPos = textDom.selectionEnd;        
    var scrollTop = textDom.scrollTop;
    textDom.value = textDom.value.substring(0, startPos) + value + textDom.value.substring(endPos, textDom.value.length);
    textDom.focus();
    textDom.selectionStart = startPos + value.length;
    textDom.selectionEnd = startPos + value.length;
    textDom.scrollTop = scrollTop;
  }else {
    textDom.value += value;
    textDom.focus();
  }
}</code></pre><p><br></p><h2 id="h2_5" pingfang="" lantinghei="" open="" hiragino="" sans="" microsoft="" wenquanyi="" micro="" white-space:="" background-color:="">六. 参考：</h2><p pingfang="" lantinghei="" open="" hiragino="" sans="" microsoft="" wenquanyi="" micro="" font-size:="" white-space:="" background-color:=""><a href="http://www.zhangxinxu.com/wordpress/2011/04/js-range-html%E6%96%87%E6%A1%A3%E6%96%87%E5%AD%97%E5%86%85%E5%AE%B9%E9%80%89%E4%B8%AD%E3%80%81%E5%BA%93%E5%8F%8A%E5%BA%94%E7%94%A8%E4%BB%8B%E7%BB%8D/" target="_blank" _href="http://www.zhangxinxu.com/wordpress/2011/04/js-range-html%E6%96%87%E6%A1%A3%E6%96%87%E5%AD%97%E5%86%85%E5%AE%B9%E9%80%89%E4%B8%AD%E3%80%81%E5%BA%93%E5%8F%8A%E5%BA%94%E7%94%A8%E4%BB%8B%E7%BB%8D/">JS Range HTML文档/文字内容选中、库及应用介绍 —— 张鑫旭</a></p><p pingfang="" lantinghei="" open="" hiragino="" sans="" microsoft="" wenquanyi="" micro="" font-size:="" white-space:="" background-color:=""><a href="http://www.zhangxinxu.com/wordpress/2010/04/%E6%96%B0%E6%B5%AA%E5%BE%AE%E5%8D%9A%E6%8F%92%E5%85%A5%E8%AF%9D%E9%A2%98%E5%90%8E%E9%83%A8%E5%88%86%E6%96%87%E5%AD%97%E9%80%89%E4%B8%AD%E7%9A%84js%E5%AE%9E%E7%8E%B0/" target="_blank" _href="http://www.zhangxinxu.com/wordpress/2010/04/%E6%96%B0%E6%B5%AA%E5%BE%AE%E5%8D%9A%E6%8F%92%E5%85%A5%E8%AF%9D%E9%A2%98%E5%90%8E%E9%83%A8%E5%88%86%E6%96%87%E5%AD%97%E9%80%89%E4%B8%AD%E7%9A%84js%E5%AE%9E%E7%8E%B0/">新浪微博插入话题后部分文字选中的js实现</a></p><p pingfang="" lantinghei="" open="" hiragino="" sans="" microsoft="" wenquanyi="" micro="" font-size:="" white-space:="" background-color:=""><a href="http://js8.in/2010/01/29/javascript%E8%8E%B7%E5%8F%96%E5%85%89%E6%A0%87%E4%BD%8D%E7%BD%AE%E4%BB%A5%E5%8F%8A%E8%AE%BE%E7%BD%AE%E5%85%89%E6%A0%87%E4%BD%8D%E7%BD%AE/" target="_blank" _href="http://js8.in/2010/01/29/javascript%E8%8E%B7%E5%8F%96%E5%85%89%E6%A0%87%E4%BD%8D%E7%BD%AE%E4%BB%A5%E5%8F%8A%E8%AE%BE%E7%BD%AE%E5%85%89%E6%A0%87%E4%BD%8D%E7%BD%AE/">javascript获取光标位置以及设置光标位置</a></p><p pingfang="" lantinghei="" open="" hiragino="" sans="" microsoft="" wenquanyi="" micro="" font-size:="" white-space:="" background-color:=""><a href="http://js8.in/2010/05/13/javascript%E5%9C%A8%E5%85%89%E6%A0%87%E4%BD%8D%E7%BD%AE%E6%8F%92%E5%85%A5%E5%86%85%E5%AE%B9/" target="_blank" _href="http://js8.in/2010/05/13/javascript%E5%9C%A8%E5%85%89%E6%A0%87%E4%BD%8D%E7%BD%AE%E6%8F%92%E5%85%A5%E5%86%85%E5%AE%B9/">javascript在光标位置插入内容</a></p><p pingfang="" lantinghei="" open="" hiragino="" sans="" microsoft="" wenquanyi="" micro="" font-size:="" white-space:="" background-color:=""><a href="http://www.quirksmode.org/dom/range_intro.html" target="_blank" _href="http://www.quirksmode.org/dom/range_intro.html">Introduction to Range</a></p><p pingfang="" lantinghei="" open="" hiragino="" sans="" microsoft="" wenquanyi="" micro="" font-size:="" white-space:="" background-color:=""><a href="http://www.quirksmode.org/dom/w3c_range.html" target="_blank" _href="http://www.quirksmode.org/dom/w3c_range.html">W3C DOM Compatibility – Range</a></p><p><br></p>
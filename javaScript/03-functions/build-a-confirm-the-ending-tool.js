// 判断 s1 是否以 s2 结尾，不能使用 endsWith() 方法
function confirmEnding(s1, s2) {
  const len1 = s1.length;
  const len2 = s2.length;
  if (len1 >= len2) {
    return s1.slice(len1 - len2) === s2;
  }
  return false;
}

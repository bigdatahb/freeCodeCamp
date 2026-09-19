// 判断一个单词是否是回文
function isPalindrome(word) {
  return word.toLowerCase() === word.toLowerCase().split("").reverse().join("");
}

// 找出一个字符串数组中所有回文的索引
function findPalindromeBreaks(words) {
  const result = [];
  if(words.length === 0) return result;
  for(let i = 0; i < words.length; ++i) {
    if(!isPalindrome(words[i])) {
      result.push(i);
    }
  }
  return result;
}

// 找出字符串数组中，所有重复出现的 具有 phraseLength 长度连续的元素 的索引
// 例如 ['the', 'cat', 'sat', 'the', 'cat'] , phraseLength = 2 的话，结果是 [0, 3]
function findRepeatedPhrases (words, phraseLength) {
  const result = [];
	// 如果要找的词组长度比字符串数组长度还大，返回空数组
  if (phraseLength >= words.length) return result;
  for(let i = 0; i + phraseLength <= words.length; i++) {
    let answer = [];
    answer.push(i); // 默认从 0 开始的具有 phraseLength 长度的连续元素是可以重复出现的
	  // 构建要找的子串
    const sub = words.slice(i, i + phraseLength).join(" ");
    for(let j = i + 1; j <= words.length - phraseLength; j++) {
		// 从下一个元素开始构建目标，看是否重复出现
      if (words.slice(j, j + phraseLength).join(" ") === sub) {
        answer.push(j);
      }
    }
    if(answer.length === 1) {
      // clear，如果没有在后续元素中找到重复出现的目标，清空这一轮结果
      answer = [];
    } else {
      result.push(...answer);
    }
  }
  return result;
}

function analyzeTexts (texts, phraseLength) {
  const result = [];
  if(texts.length === 0) return result;
  for(const item of texts) {
    const repeatedPhrase = findRepeatedPhrases(item, phraseLength);
    const palindromeBreaks = findPalindromeBreaks(item);
    result.push({repeatedPhrases: repeatedPhrase, palindromeBreaks: palindromeBreaks});
  }
  return result;
}

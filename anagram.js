function isAnagram(s, t) {
  if (s.length != t.length) {
    return false
  }
    
  let counter = 0
  let blackbox = []
  
  

}
console.log(isAnagram('anagram', 'nagaram'))  // true
console.log(isAnagram('rat', 'car'))          // false
console.log(isAnagram('listen', 'silent'))    // true
console.log(isAnagram('aab', 'aba'))           // true
console.log(isAnagram('aab', 'abb'))           // false
console.log(isAnagram('aa', 'ab'))             // false

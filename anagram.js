function isAnagram(s, t) {
  if (s.length != t.length) {
    return false
  }
    
  let counter = 0
  let blackbox = []
  for (j=0; j< s.length;j++){
    let alreadyfound= false
  }
  

}
console.log(isAnagram('anagram', 'nagaram'))  // true
console.log(isAnagram('rat', 'car'))          // false
console.log(isAnagram('listen', 'silent'))    // true
console.log(isAnagram('aab', 'aba'))           // true
console.log(isAnagram('aab', 'abb'))           // false
console.log(isAnagram('aa', 'ab'))             // false

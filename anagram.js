function isAnagram(s, t) {
  if (s.length != t.length) {
    return false
  }
    
  let counter = 0
  let blackbox = []
  for (i=0; i< s.length;i++){
    let alreadyfound= false
    for(j=0;j< t.length;j++){
      
    }
  }
  

}
console.log(isAnagram('anagram', 'nagaram'))  // true
console.log(isAnagram('rat', 'car'))          // false
console.log(isAnagram('listen', 'silent'))    // true
console.log(isAnagram('aab', 'aba'))           // true
console.log(isAnagram('aab', 'abb'))           // false
console.log(isAnagram('aa', 'ab'))             // false

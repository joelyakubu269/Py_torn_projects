function isAnagram(s, t) {
  if (s.length != t.length) {
    return false
  }
    
  let counter = 0
  let blackbox = []
  for (i=0; i< s.length;i++){
    let alreadyfound= false // we are assuming that a match is not found at the beginning
    for(j=0;j< t.length;j++){
      if (s[i]==t[j]) {
        alreadyused= false // i am assuming the index has not been used(i.e because of duplicates)
        for (let k=0;k< blackbox.length;k++) {
          
        }
      }
      
    }
  }
  

}
console.log(isAnagram('anagram', 'nagaram'))  // true
console.log(isAnagram('rat', 'car'))          // false
console.log(isAnagram('listen', 'silent'))    // true
console.log(isAnagram('aab', 'aba'))           // true
console.log(isAnagram('aab', 'abb'))           // false
console.log(isAnagram('aa', 'ab'))             // false

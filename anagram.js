function isAnagram(s, t) {
  if (s.length != t.length) {
    return false
  }
  counter= 0
  let blackbox= []
  let i= 0
  while ( i<s.length) {
    for (let j=0; j< s.length;j++){
        if (s[i] == t[j]) {
                counter++
                i++
        }
        
        
    }
    
  }
  if (counter == s.length) {
    return true
  }else {
    return false
  }
}
console.log(isAnagram('anagram', 'nagaram'))  // true
console.log(isAnagram('rat', 'car'))          // false
console.log(isAnagram('listen', 'silent'))    // true
function isAnagram(s, t) {
  if (s.length != t.length) {
    return false
  }
  counter= 0
  let blackbox= []
  for (let i=0; i<s.length;i++) {
    for (let j=0; j< s.length;j++){
        if (s[i] == t[j]) {
                blackbox.push(j)
        }
    }
    for (let k=0; k< blackbox.length;k++) {
        if (blackbox[k]== j) {
            alreadyused= true
        }else{
            alreadyused= false
        }
        if (!alreadyused) {
            counter++
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
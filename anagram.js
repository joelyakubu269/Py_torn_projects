function isAnagram(s, t) {
  if (s.length != t.length) {
    return false
  }

  let counter = 0
  let blackbox = []

  for (let i = 0; i < s.length; i++) {
    let alreadyFound = false

    for (let j = 0; j < t.length; j++) {

      // First: do the characters match?
      if (s[i] == t[j]) {

        // Assume this j has not been used
        let alreadyUsed = false

        // Check if j is already inside blackbox
        for (let k = 0; k < blackbox.length; k++) {
          if (blackbox[k] == j) {
            alreadyUsed = true
            break
          }
        }

        // If j has not been used, accept the match
        if (!alreadyUsed) {
          blackbox.push(j)
          counter++
          alreadyFound = true
          break
        }
      }
    }

    // No available matching character was found for s[i]
    if (!alreadyFound) {
      return false
    }
  }

  return counter == s.length
}

console.log(isAnagram('anagram', 'nagaram'))  // true
console.log(isAnagram('rat', 'car'))          // false
console.log(isAnagram('listen', 'silent'))    // true
console.log(isAnagram('aab', 'aba'))           // true
console.log(isAnagram('aab', 'abb'))           // false
console.log(isAnagram('aa', 'ab'))             // false

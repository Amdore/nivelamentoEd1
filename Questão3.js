function reverseWord(word){
  let wordArr = []
  for(const i of word){
    wordArr.push(i)
  }
 
  let rev = []
 
  for(const i of word){
    rev.push(wordArr.pop())
  }
  return rev
}
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms

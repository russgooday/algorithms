function computeLPS(needle) {
    const len = needle.length
    const lps = Array.from({ length: len }, () => 0);
    let i = 0
    let j = 1

    while (j < len) {
      if (needle[j] === needle[i]) {
        i += 1
        lps[j] = i
        j += 1
      } else if (i === 0) {
        j += 1
      } else {
        i = lps[i-1]
      }
    }

    return lps
}

function KMPSearch(needle, haystack) {
  const lenHaystack = haystack.length;
  const lenNeedle = needle.length;
  const lps = computeLPS(needle)


  let i = 0;
  let j = 0;

  while (j < lenHaystack) {
    if (needle[i] === haystack[j]) {
      i += 1
      j += 1
    } else if (i === 0) {
      j += 1
    } else {
      i = lps[i-1]
    }

    if (i === lenNeedle) {
      return [j - lenNeedle, j]
    }
  }
  return -1
}

function KMPSearchAll(needle, haystack) {
  let lenHaystack = haystack.length;
  const lenNeedle = needle.length;
  const lps = computeLPS(needle)
  const found = []

  let i = 0;
  let j = 0;

  while (j < lenHaystack) {
    if (needle[i] === haystack[j]) {
      i += 1
      j += 1
    } else if (i === 0) {
      j += 1
    } else {
      i = lps[i-1]
    }

    if (i === lenNeedle) {
      found.push([j - lenNeedle, j])
      if ((lenHaystack - j) < lenNeedle) {
        break
      }
    }
  }

  return found
}

console.log(computeLPS('aabaaac'))
console.log(KMPSearchAll('onions', 'onionionslponionslp'))
console.log('onionionslp'.slice(...KMPSearch('onions', 'onionionslp')))
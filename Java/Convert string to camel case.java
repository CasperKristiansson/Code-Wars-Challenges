package Java;

// https://www.codewars.com/kata/517abf86da9663f1d2000003/train/java

class Solution{

  static String toCamelCase(String s){
    String[] result = s.replace("-", " ").replace("_", " ").split(" ");
    for(int i = 1; i < result.length; i++) {
      result[i] = result[i].substring(0, 1).toUpperCase() + result[i].substring(1);
    }
    return String.join("", result);
  }
}

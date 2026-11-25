import PDFKit
let d = PDFDocument(url: URL(fileURLWithPath: CommandLine.arguments[1]))!
print("PAGES", d.pageCount)
for i in 0..<d.pageCount {
  let t = d.page(at: i)?.string ?? ""
  var r = t.startIndex..<t.endIndex
  while let m = t.range(of: "zqx[0-9]+qz", options: .regularExpression, range: r) {
    print(t[m], i+1); r = m.upperBound..<t.endIndex
  }
}

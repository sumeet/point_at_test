Find a test path name by pointing at it inside your editor.

```python
class MyTest(TestCase):

    def test_something(self):
        self.assertEqual(2, 1 + 1)
```

Hover your cursor over the function signature for `test_something` to run
`MyTest.test_something`.

Hover over the class signature for `MyTest` to run `MyTest`.

If pointing to anything else, run the entire module.


Instructions for Vim:

```vim
function StoreTestPath(filename, lineno)
    let g:t= a:filename
    let g:f = system("python ~/point_at_test/point_at_test.py ".shellescape(a:filename)." ".shellescape(a:lineno))
    let g:f=substitute(strtrans(g:f),'\^@',' ','g')
    echo g:t g:f
endfun
map <Leader>s :call StoreTestPath(expand("%"), line("."))<CR>

function RunTests(filename, test_path)
    if a:test_path != ' '
        let full_test_path = a:filename.":".a:test_path
    else
        let full_test_path = a:filename
    endif
    exec ":!nosetests ".full_test_path
endfun
map <Leader>t :call RunTests(g:t, g:f)<CR>
```

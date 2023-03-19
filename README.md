# python-supporter

https://pypi.org/project/python-supporter
<pre>
pip install python-supporter
</pre>

```
import python_supporter

#python_supporter.logging.basicConfig(python_supporter.logging.ERROR)
#python_supporter.logging.basicConfig(python_supporter.logging.INFO)
python_supporter.logging.basicConfig(python_supporter.logging.DEBUG)
#python_supporter.logging.basicConfig(python_supporter.logging.ERROR, filename='log.txt')
#python_supporter.logging.basicConfig(python_supporter.logging.INFO, filename='log.txt')
#python_supporter.logging.basicConfig(python_supporter.logging.DEBUG, filename='log.txt')

python_supporter.logging.error('This is error message') #
python_supporter.logging.info('This is info message') #
python_supporter.logging.debug('This is debug message') #

Cufflinks is an interactive visualization library that's open source.

cufflinks is a library for easy interactive Pandas charting with Plotly.

--------------------------
Installation:
--------------------------

conda install plotly
pip install cufflinks --upgrade
jupyter labextension install @jupyterlab/plotly-extension


--------------------------
Doc
--------------------------

Plotly for pandas doc is here: https://plot.ly/pandas/

--------------------------
Save plotly in html
--------------------------

```python
# Show
df.iplot()
# offline mode: Save iplot in export_example.html
df.iplot(filename='export_example', asUrl=True)
```



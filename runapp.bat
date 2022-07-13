@echo off

python -m streamlit run main.py --logger.enableRich=true --server.headless=true --server.runOnSave=true --theme.base=dark --theme.font=monospace

:: python -m streamlit run --help
::
::   --logger.enableRich BOOLEAN     Controls whether uncaught app exceptions  
::                                   are logged via the rich library.
:: 
::                                   If True and if rich is installed,
::                                   exception tracebacks will be logged with  
::                                   syntax highlighting and formatting. Rich  
::                                   tracebacks are easier to read and show    
::                                   more code than standard Python
::                                   tracebacks.
:: 
::                                   If set to False, the default Python       
::                                   traceback formatting will be used.  [env  
::                                   var: STREAMLIT_LOGGER_ENABLE_RICH]
:: 
::   --server.headless BOOLEAN       If false, will attempt to open a browser  
::                                   window on start.
:: 
::                                   Default: false unless (1) we are on a     
::                                   Linux box where DISPLAY is unset, or (2)  
::                                   we are running in the Streamlit Atom      
::                                   plugin.  [env var:
::                                   STREAMLIT_SERVER_HEADLESS]
:: 
::   --server.runOnSave BOOLEAN      Automatically rerun script when the file  
::                                   is modified on disk.
::
::                                   Default: false  [env var:
::                                   STREAMLIT_SERVER_RUN_ON_SAVE] 
:: 
::   --theme.base TEXT               The preset Streamlit theme that your custom
::                                   theme inherits from. One of "light" or     
::                                   "dark".  [env var: STREAMLIT_THEME_BASE]
::
::   --theme.font TEXT               Font family for all text in the app,
::                                   except code blocks. One of "sans serif",
::                                   "serif", or "monospace".  [env var:
::                                   STREAMLIT_THEME_FONT]

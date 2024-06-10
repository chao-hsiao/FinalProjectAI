mkdir -p ~/.streamlit/

echo "\
[general]
email = \"xsyao.ch.cs10@nycu.edu.tw\"
" > ~/.streamlit/credentials.toml

echo "\
[server]
headless = true
enableCORS=false
port = 80
" > ~/.streamlit/config.toml

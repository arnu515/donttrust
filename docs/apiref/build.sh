if [ -d build ]; then
    echo "Build directory already exists. Purging..."
    rm -r build
fi
cd ../..
source venv/bin/activate
sphinx-apidoc -f -o docs/apiref/source/docstrings donttrust
cd docs/apiref
make html
mv build/html build/apiref

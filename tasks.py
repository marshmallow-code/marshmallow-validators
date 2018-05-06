# -*- coding: utf-8 -*-
import os
import sys
import webbrowser

from invoke import task, run
import pytest

docs_dir = 'docs'
build_dir = os.path.join(docs_dir, '_build')

@task
def test(ctx):
    flake(ctx)
    retcode = pytest.main([])
    sys.exit(retcode)

@task
def flake(ctx):
    """Run flake8 on codebase."""
    run('flake8 .', echo=True)

@task
def watch(ctx):
    """Run tests when a file changes."""
    import pytest
    errcode = pytest.main(['-f'])
    sys.exit(errcode)

@task
def clean(ctx):
    run("rm -rf build")
    run("rm -rf dist")
    run("rm -rf marshmallow-validators.egg-info")
    clean_docs(ctx)
    print("Cleaned up.")

@task
def clean_docs(ctx):
    run("rm -rf %s" % build_dir)

@task
def browse_docs(ctx):
    path = os.path.join(build_dir, 'index.html')
    webbrowser.open_new_tab(path)

@task
def docs(ctx, clean=False, browse=False, watch=False):
    """Build the docs."""
    if clean:
        clean_docs()
    run("sphinx-build %s %s" % (docs_dir, build_dir), echo=True)
    if browse:
        browse_docs()
    if watch:
        watch_docs()

@task
def watch_docs(ctx):
    """Run build the docs when a file changes."""
    try:
        import sphinx_autobuild  # noqa
    except ImportError:
        print('ERROR: watch task requires the sphinx_autobuild package.')
        print('Install it with:')
        print('    pip install sphinx-autobuild')
        sys.exit(1)
    run('sphinx-autobuild {} {}'.format(docs_dir, build_dir), pty=True)

@task
def readme(ctx, browse=False):
    run('rst2html.py README.rst > README.html')
    if browse:
        webbrowser.open_new_tab('README.html')

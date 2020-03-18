from setuptools import setup, find_packages

version = "1.3.4"

setup(
    name="rt.simpleslider",
    version=version,
    description="A really simple Plone slider based on basic-slider.com",
    long_description=open("README.rst").read()
    + "\n"
    + open("HISTORY.txt").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: Addon",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    keywords="plone slider",
    author="RedTurtle team",
    author_email="svilplone@redturtle.it",
    url="http://www.redturtle.it",
    license="GPL",
    packages=find_packages(exclude=["ez_setup"]),
    namespace_packages=["rt"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        # -*- Extra requirements: -*-
    ],
    entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
)

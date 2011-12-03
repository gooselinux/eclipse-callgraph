#!/bin/sh
usage='usage: $0 <tag>'
name=eclipse-callgraph
tag=R0_5_0
plugins=`echo org.eclipse.linuxtools.callgraph{,.core,.launch,-feature}`
tar_name=$name-fetched-src-$tag

fetch_cmd="svn export http://dev.eclipse.org/svnroot/technology/org.eclipse.linuxtools/systemtap/tags/$tag/"

rm -fr $tar_name && mkdir $tar_name
pushd $tar_name

# Fetch plugins
for plugin in $plugins; do
	$fetch_cmd$plugin
done

popd
# create archive
tar -cjf $tar_name.tar.bz2 $tar_name


# Copyright (c) SWAN Development Team.
# Author: Omar.Zapata@cern.ch 2021

"""
This file has the configurable class SwanConfig to parse options from command line.
"""
from traitlets import Unicode
from traitlets.config import Configurable
import os


class SwanConfig(Configurable):
    """
    Class to parse configuration options from command line. 
    """
    stacks_path = Unicode(
        os.path.dirname(os.path.abspath(__file__)) + '/stacks',
        config=True,
        help="The path to the folder containing stack configuration")
    kernel_resources = Unicode(
        os.path.dirname(os.path.abspath(__file__)) +
        '/kernelmanager/resources',
        config=True,
        help="The path to the folder containg the resources to add to the kernel"
    )
    project_file_name = Unicode(
        '.swanproject',
        config=False,
        help="Project file name.")
    userscript_file_name = Unicode(
        '.userscript',
        config=False,
        help="User script file name.")
    projects_folder_name = Unicode(
        "SWAN_projects",
        config=False,
        help="Projects folder name.")
    projects_folder_path = Unicode(
        os.path.join(os.environ["HOME"],projects_folder_name.default_value),
        config=False,
        help="Projects full path for SWAN_projects.")

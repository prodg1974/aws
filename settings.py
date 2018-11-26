import os
from os.path import join, dirname
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path)



class Config(object):
    os.path.join(basedir,'app.db')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or'sqlite:///'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_URL = os.environ.get("DATABASE_URL")

    SQL_LOGIN = os.environ.get("SQL_LOGIN")
    SQL_PWD = os.environ.get("SQL_PWD")
    # SQL_KEY = os.environ.get("CMP_KEY")

    CMP_LOGIN = os.environ.get("CMP_LOGIN")
    CMP_PWD = os.environ.get("CMP_PWD")
    CMP_KEY = os.environ.get("CMP_KEY")
    
    AIY_LOGIN = os.environ.get("AIY_LOGIN")
    AIY_PWD = os.environ.get("AIY_PWD")
    AIY_KEY = os.environ.get("AIY_KEY")


    ASC_LOGIN = os.environ.get("ASC_LOGIN")
    ASC_PWD = os.environ.get("ASC_PWD")
    ASC_KEY = os.environ.get("ASC_KEY")

    CRW_LOGIN = os.environ.get("CRW_LOGIN")
    CRW_PWD = os.environ.get("CRW_PWD")
    CRW_KEY = os.environ.get("CRW_KEY")


    IMI_LOGIN = os.environ.get("IMI_LOGIN")
    IMI_PWD = os.environ.get("IMI_PWD")
    IMI_KEY = os.environ.get("IMI_KEY")

    WFI_LOGIN = os.environ.get("WFI_LOGIN")
    WFI_PWD = os.environ.get("WFI_PWD")
    WFI_KEY = os.environ.get("WFI_KEY")

    BRU_LOGIN = os.environ.get("BRU_LOGIN")
    BRU_PWD = os.environ.get("BRU_PWD")
    BRU_KEY = os.environ.get("BRU_KEY")

    COM_LOGIN = os.environ.get("COM_LOGIN")
    COM_PWD = os.environ.get("COM_PWD")
    COM_KEY = os.environ.get("COM_KEY")

    BOM_LOGIN = os.environ.get("BOM_LOGIN")
    BOM_PWD = os.environ.get("BOM_PWD")
    BOM_KEY = os.environ.get("BOM_KEY")

    ACH_LOGIN = os.environ.get("ACH_LOGIN")
    ACH_PWD = os.environ.get("ACH_PWD")
    ACH_KEY = os.environ.get("ACH_KEY")

    SDS_LOGIN = os.environ.get("SDS_LOGIN")
    SDS_PWD = os.environ.get("SDS_PWD")
    SDS_KEY = os.environ.get("SDS_KEY")
 
    EEP_LOGIN = os.environ.get("EEP_LOGIN")
    EEP_PWD = os.environ.get("EEP_PWD")
    EEP_KEY = os.environ.get("EEP_KEY")
    
    SEI_LOGIN = os.environ.get("SEI_LOGIN")
    SEI_PWD = os.environ.get("SEI_PWD")
    SEI_KEY = os.environ.get("SEI_KEY")
    
    CHI_LOGIN = os.environ.get("CHI_LOGIN")
    CHI_PWD = os.environ.get("CHI_PWD")
    CHI_KEY = os.environ.get("CHI_KEY")
#SFTP Logins
    ASC_ABS_LOGIN = os.environ.get("ASC_ABS_LOGIN")
    ASC_ABS_ACCOUNT = os.environ.get("ASC_ABS_ACCOUNT")
    ASC_ABS_PWD = os.environ.get("ASC_ABS_PWD")
    ASC_ABS_PORT = os.environ.get("ASC_ABS_PORT")

    ASC_BCBS_LOGIN = os.environ.get("ASC_BCBS_LOGIN")
    ASC_BCBS_ACCOUNT = os.environ.get("ASC_BCBS_ACCOUNT")
    ASC_BCBS_PWD = os.environ.get("ASC_BCBS_PWD")
    ASC_BCBS_PORT = os.environ.get("ASC_BCBS_PORT")

    IMI_EFX_LOGIN = os.environ.get("IMO_EFX_LOGIN")
    IMI_EFX_ACCOUNT = os.environ.get("IMI_EFX_ACCOUNT")
    IMI_EFX_PWD = os.environ.get("IMI_EFX_PWD")
    IMI_EFX_PORT = os.environ.get("IMI_EFX_PWD")

    ACH_PVT_LOGIN = os.environ.get("ACH_PVT_LOGIN")
    ACH_PVT_ACCOUNT = os.environ.get("ACH_PVT_ACCOUNT")
    ACH_PVT_PWD = os.environ.get("ACH_PVT_PWD")
    ACH_PVT_PORT = os.environ.get("ACH_PVT_PORT")

    REDBRICK_LOGIN = os.environ.get("REDBRICK_LOGIN")
    REDBRICK_ACCOUNT = os.environ.get("REDBRICK_ACCOUNT")
    REDBRICK_PWD = os.environ.get("REDBRICK_PWD")
    REDBRICK_PORT = os.environ.get("REDBRICK_PORT")

    REDBRICK_PVD_LOGIN = os.environ.get("REDBRICK_PVD_LOGIN")
    REDBRICK_PVD_ACCOUNT = os.environ.get("REDBRICK_PVD_ACCOUNT")
    REDBRICK_PVD_PWD = os.environ.get("REDBRICK_PVD_PWD")
    REDBRICK_PVD_PORT = os.environ.get("REDBRICK_PVD_PORT")

    PSR_TEST_LOGIN = os.environ.get("PSR_TEST_LOGIN")
    PSR_TEST_ACCOUNT = os.environ.get("PSR_TEST_ACCOUNT")
    PSR_TEST_PWD = os.environ.get("PSR_TEST_PWD")
    PSR_TEST_PORT = os.environ.get("PSR_TEST_PORT")

    TEST_LOGIN=os.environ.get("TEST_LOGIN")
    TEST_ACCOUNT=os.environ.get("TEST_ACCOUNT")
    TEST_PWD=os.environ.get("TEST_PWD")
    TEST_PORT=os.environ.get("TEST_PORT")

# Database Logins
    REDSHIFT_LOGIN = os.environ.get("REDSHIFT_LOGIN")
    REDSHIFT_PORT = os.environ.get("REDSHIFT_PORT")
    REDSHIFT_URL = os.environ.get("REDSHIFT_URL")
    REDSHIFT_PWD = os.environ.get("REDSHIFT_PWD")
    REDSHIFT_DB = os.environ.get("REDSHIFT_DB")

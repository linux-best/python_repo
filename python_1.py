from loguru import logger

path="/var/lib/jenkins/workspace/my_python_Job/file10"

logger.add(path ,
           format="<yellow>{time: MMMM D, YYYY - HH:mm:ss}</yellow> -- <green>{level}</green> -- <level>{message}</level> {extra}",
           level="DEBUG"
)

logger.success("Build Execute !")

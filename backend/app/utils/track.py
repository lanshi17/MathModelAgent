from litellm.integrations.custom_logger import CustomLogger
import litellm
from app.utils.log_util import logger


class AgentMetrics(CustomLogger):
    #### ASYNC ####

    async def async_log_success_event(self, kwargs, response_obj, start_time, end_time):
        try:
            # response_cost = kwargs.get("response_cost", 0)
            # print("streaming response_cost", response_cost)
            agent_name = kwargs.get("litellm_params", {}).get("metadata", {}).get("agent_name", "unknown")
            logger.debug(f"LiteLLM Success - Agent: {agent_name}")
        except Exception as e:
            logger.warning(f"LiteLLM Success 日志记录失败: {str(e)}")

    async def async_log_failure_event(self, kwargs, response_obj, start_time, end_time):
        try:
            # 获取更多错误信息
            agent_name = kwargs.get("litellm_params", {}).get("metadata", {}).get("agent_name", "unknown")
            model = kwargs.get("model", "unknown")
            error_msg = getattr(response_obj, 'message', str(response_obj)) if response_obj else "Unknown error"

            logger.error(f"LiteLLM 异步失败 - Agent: {agent_name}, Model: {model}, Error: {error_msg}")
        except Exception as e:
            logger.error(f"LiteLLM 异步失败 - 无法获取详细信息: {str(e)}")


# 全局指标收集器实例
agent_metrics = AgentMetrics()

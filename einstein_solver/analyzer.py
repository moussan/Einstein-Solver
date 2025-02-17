from PyQt6.QtCore import QThread, pyqtSignal
import json
import asyncio
import aiohttp
from typing import Optional, Dict, Any
from .utils import MetricData, APIConfig

class LLMAnalyzer(QThread):
    """Handles LLM analysis in a separate thread to keep UI responsive"""
    finished = pyqtSignal(str)
    error = pyqtSignal(str)
    
    def __init__(self, metric_data: MetricData, api_config: APIConfig, analysis_type: str):
        super().__init__()
        self.metric_data = metric_data
        self.api_config = api_config
        self.analysis_type = analysis_type
        self._should_stop = False
    
    def stop(self):
        """Stop the analysis"""
        self._should_stop = True
    
    def get_prompt(self) -> str:
        """Generate appropriate prompt based on analysis type"""
        base_prompt = f"""You are a physics expert specialized in general relativity. 
        Analyzing this metric tensor:
        {json.dumps(self.metric_data.components, indent=2)}
        Coordinates: {', '.join(self.metric_data.coordinates)}
        """
        
        prompts = {
            "validate": base_prompt + """
                Please analyze for:
                1. Signature consistency
                2. Symmetry requirements
                3. Physical meaningfulness
                4. Common errors or issues
                5. Potential simplifications
                
                Provide your analysis in a clear, structured format.
                """,
            "interpret": base_prompt + """
                Please interpret this metric tensor and explain:
                1. What type of spacetime it represents
                2. Its physical significance
                3. Any special properties or symmetries
                4. Known solutions it might be related to
                5. Potential physical applications
                
                Provide your interpretation in clear, physics-focused language.
                """,
            "suggest": base_prompt + """
                Please suggest:
                1. Possible modifications to explore
                2. Additional terms to consider
                3. Alternative coordinate systems
                4. Related metrics to compare with
                5. Potential physical scenarios to study
                
                Provide practical, physics-based suggestions.
                """
        }
        
        return prompts.get(self.analysis_type, base_prompt)
    
    async def _make_api_request(self, session: aiohttp.ClientSession, attempt: int = 1) -> Dict[str, Any]:
        """Make API request with retry logic"""
        try:
            async with session.post(
                f"{self.api_config.api_url}/analyze",
                json={
                    "prompt": self.get_prompt(),
                    "metric_data": self.metric_data.to_json(),
                    "analysis_type": self.analysis_type
                },
                headers=self.api_config.get_headers(),
                timeout=self.api_config.timeout
            ) as response:
                if response.status == 200:
                    return await response.json()
                elif response.status == 429 and attempt < self.api_config.max_retries:
                    # Rate limit hit, wait and retry
                    await asyncio.sleep(2 ** attempt)
                    return await self._make_api_request(session, attempt + 1)
                else:
                    response.raise_for_status()
                    
        except asyncio.TimeoutError:
            if attempt < self.api_config.max_retries:
                return await self._make_api_request(session, attempt + 1)
            raise
    
    async def analyze(self) -> str:
        """Perform the analysis"""
        try:
            async with aiohttp.ClientSession() as session:
                result = await self._make_api_request(session)
                return result.get('analysis', 'No analysis provided')
                
        except Exception as e:
            raise RuntimeError(f"Analysis failed: {str(e)}")
    
    def run(self):
        """Run the analysis in a separate thread"""
        try:
            if self._should_stop:
                return
                
            # Create event loop for async operations
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            # Run analysis
            result = loop.run_until_complete(self.analyze())
            
            if self._should_stop:
                return
                
            # Emit result
            self.finished.emit(result)
            
        except Exception as e:
            if not self._should_stop:
                self.error.emit(str(e))
        finally:
            loop.close()

class ResultsAnalyzer:
    """Analyzes calculation results for physical significance"""
    def __init__(self, metric_data: MetricData):
        self.metric_data = metric_data
    
    def analyze_signature(self) -> str:
        """Analyze metric signature"""
        try:
            # Implementation would go here
            # This is a placeholder that would need real implementation
            return "Metric signature analysis not implemented"
        except Exception as e:
            return f"Signature analysis failed: {str(e)}"
    
    def analyze_symmetries(self) -> str:
        """Analyze metric symmetries"""
        try:
            # Implementation would go here
            # This is a placeholder that would need real implementation
            return "Symmetry analysis not implemented"
        except Exception as e:
            return f"Symmetry analysis failed: {str(e)}"
    
    def analyze_singularities(self) -> str:
        """Analyze potential singularities"""
        try:
            # Implementation would go here
            # This is a placeholder that would need real implementation
            return "Singularity analysis not implemented"
        except Exception as e:
            return f"Singularity analysis failed: {str(e)}"
    
    def get_full_analysis(self) -> str:
        """Get complete analysis of results"""
        analyses = [
            ("Signature Analysis", self.analyze_signature()),
            ("Symmetry Analysis", self.analyze_symmetries()),
            ("Singularity Analysis", self.analyze_singularities())
        ]
        
        return "\n\n".join(f"{title}:\n{content}" for title, content in analyses)

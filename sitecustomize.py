import sys
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent

RAG_PROGRAMS = ROOT / "RAG_programs"
SHARED = ROOT / "shared"
POLICY_PILOT = ROOT / "advanced_rag" / "policy_pilot_project"

sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(RAG_PROGRAMS))
sys.path.insert(0, str(POLICY_PILOT))

os.chdir(SHARED)